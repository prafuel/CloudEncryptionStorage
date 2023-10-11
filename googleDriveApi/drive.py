from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Set the path to your JSON key file
JSON_KEY_FILE = "../json_key/southern-branch-377015.json"

# Authenticate with the Google Drive API using the service account key
creds = service_account.Credentials.from_service_account_file(JSON_KEY_FILE, scopes=['https://www.googleapis.com/auth/drive'])
drive_service = build('drive', 'v3', credentials=creds)

# Define the file to upload
file_name = 'requirement.txt'
file_path = '../requirement.txt'

# Upload the file to Google Drive
file_metadata = {
    'name': file_name
}
media = MediaFileUpload(file_path, resumable=True)
file = drive_service.files().create(media_body=media, body=file_metadata).execute()

print(f'File ID: {file["id"]}')
