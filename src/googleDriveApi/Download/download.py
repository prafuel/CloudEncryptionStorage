
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

def download_file(file_id : str, JSON_KEY_FILE : str, file_name : str) -> None:
    # Authenticate with the Google Drive API using the service account key
    creds = service_account.Credentials.from_service_account_file(JSON_KEY_FILE, scopes=['https://www.googleapis.com/auth/drive'])
    drive_service = build('drive', 'v3', credentials=creds)

    # Define the local path where you want to save the downloaded file
    local_file_path = f'/home/version/Desktop/cc/#test/Encrypted/{file_name}.txt'

    # Download the file from Google Drive
    request = drive_service.files().get_media(fileId=file_id)
    fh = open(local_file_path, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print(f"Download {int(status.progress() * 100)}%.")

    print(f"Downloaded file to {local_file_path}")


if __name__ == "__main__" :
    file_id = "13MkVcS-yMiCEo7tcuRXe8qBooqNA3SY_"
    JSON_KEY_FILE = '../../json_key/southern-branch-377015.json'
    file_name = "temp1"

    download_file(file_id=file_id, JSON_KEY_FILE=JSON_KEY_FILE, file_name=file_name)