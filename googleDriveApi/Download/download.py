
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload


# Set the path to your JSON key file
JSON_KEY_FILE = '../../json_key/southern-branch-377015.json'

# Authenticate with the Google Drive API using the service account key
creds = service_account.Credentials.from_service_account_file(JSON_KEY_FILE, scopes=['https://www.googleapis.com/auth/drive'])
drive_service = build('drive', 'v3', credentials=creds)

# Define the File ID of the file you want to download
file_id = '1Tb0Y3adqRuaz7j1CEeKhMknVd74qyzzi'

# Define the local path where you want to save the downloaded file
local_file_path = './done.txt'

# Download the file from Google Drive
request = drive_service.files().get_media(fileId=file_id)
fh = open(local_file_path, 'wb')
downloader = MediaIoBaseDownload(fh, request)
done = False
while done is False:
    status, done = downloader.next_chunk()
    print(f"Download {int(status.progress() * 100)}%.")

print(f"Downloaded file to {local_file_path}")
