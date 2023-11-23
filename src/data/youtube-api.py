import os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import google.auth
from google.oauth2 import service_account


# API_SERVICE_NAME = 'youtubeAnalytics'
# API_VERSION = 'v2'
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'


def youtube_oauth2_login(client_secrets_file):
    # Define the scope
    scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
    # scopes = ['https://www.googleapis.com/auth/yt-analytics.readonly']

    # Get credentials and create an API client
    flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
    credentials = flow.run_local_server(port=56771)

    # Load credentials from the environment variable
    # credentials = service_account.Credentials.from_service_account_file(
    #     os.environ.get('GOOGLE_APPLICATION_CREDENTIALS'), scopes=scopes)
    
    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)

def get_watch_history(youtube):
    # Replace with your channel ID
    channel_id = 'UCeToWA4eh8kzRWjz-_6AZtg'
    
    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id=channel_id
    )
    response = request.execute()

    print(response)


    # Get the watch history playlist ID
    # request = youtube.channels().list(part='contentDetails', id=channel_id)
    # response = request.execute()
    # print(response)
    # watch_history_id = response['items'][0]['contentDetails']['relatedPlaylists']['watchHistory']

    # # Retrieve watch history videos
    # request = youtube.playlistItems().list(part='snippet', playlistId=watch_history_id, maxResults=50)
    # response = request.execute()

    # for item in response['items']:
    #     title = item['snippet']['title']
    #     video_id = item['snippet']['resourceId']['videoId']
    #     print(f'{title} (Video ID: {video_id})')

def execute_api_request(client_library_function, **kwargs):
    response = client_library_function(**kwargs).execute()

    print(response)


if __name__ == "__main__":
    # client_secrets_file = 'g-dev-cred.json'  # Path to your client_secrets.json file
    client_secrets_file = 'gdev-ytanalytics-cred.json'  # Path to your client_secrets.json file
    youtube = youtube_oauth2_login(client_secrets_file)
    get_watch_history(youtube)
    # execute_api_request(
    #     youtube.reports().query,
    #     ids = 'channel==UCeToWA4eh8kzRWjz-_6AZtg',
    #     startDate='2023-11-11',
    #     endDate='2023-11-17',
    #     metrics='estimatedMinutesWatched,views,likes,subscribersGained',
    #     dimensions='day',
    #     sort='day'
    # )