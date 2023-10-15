from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Set the path to your JSON key file
JSON_KEY_FILE = "cc/src/json_key/southern-branch-377015.json"


# Define the file to upload
file_name = 'requirements.txt'
file_path = 'requirements.txt'


def on_drive(JSON_KEY_PATH: str, file_path: str):
    # Extract file name from provided file path
    file_name = file_path.split("/").pop(len(file_path.split("/")) - 1)

    # Authenticate with the Google Drive API using the service account key
    creds = service_account.Credentials.from_service_account_file(
        JSON_KEY_PATH, scopes=['https://www.googleapis.com/auth/drive'])
    drive_service = build('drive', 'v3', credentials=creds)

    # Upload the file to Google Drive
    file_metadata = {
        'name': file_name
    }
    media = MediaFileUpload(file_path, resumable=True)
    file = drive_service.files().create(
        media_body=media, body=file_metadata).execute()

    print(f'File ID: {file["id"]}')

    file_id = open("src/googleDriveApi/file_id.txt", "a")
    file_id.write(file_name + ": " + file['id'] + "\n")
    file_id.close()
    return file["id"]


# if __name__ == "__main__":

#     JSON_KEY_FILE = "../json_key/southern-branch-377015.json"
#     file_path = "../#test/text1.txt"
#     on_drive(JSON_KEY_FILE, file_path)
