import os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import google.auth
from google.oauth2 import service_account


def youtube_oauth2_login(client_secrets_file):
    # Define the scope
    scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

    # Get credentials and create an API client
    # flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
    # credentials = flow.run_local_server(port=0)

    # Load credentials from the environment variable
    credentials = service_account.Credentials.from_service_account_file(
        os.environ.get('GOOGLE_APPLICATION_CREDENTIALS'), scopes=scopes)
    
    return build('youtube', 'v3', credentials=credentials)

def get_watch_history(youtube):
    # Replace with your channel ID
    channel_id = 'UCeToWA4eh8kzRWjz-_6AZtg'

    # Get the watch history playlist ID
    request = youtube.channels().list(part='contentDetails', id=channel_id)
    response = request.execute()
    watch_history_id = response['items'][0]['contentDetails']['relatedPlaylists']['watchHistory']

    # Retrieve watch history videos
    request = youtube.playlistItems().list(part='snippet', playlistId=watch_history_id, maxResults=50)
    response = request.execute()

    for item in response['items']:
        title = item['snippet']['title']
        video_id = item['snippet']['resourceId']['videoId']
        print(f'{title} (Video ID: {video_id})')

if __name__ == "__main__":
    client_secrets_file = 'g-dev-cred.json'  # Path to your client_secrets.json file
    youtube = youtube_oauth2_login(client_secrets_file)
    get_watch_history(youtube)
