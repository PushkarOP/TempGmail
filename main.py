import os
import pickle
import base64
import time
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import random
import string

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

BASE_EMAIL = "change_here@gmail.com"

def get_email_content(msg):
    """Extracts the email content from the message."""
    if 'data' in msg['payload']['body']:
        return base64.urlsafe_b64decode(msg['payload']['body']['data']).decode('utf-8')
    elif 'parts' in msg['payload']:
        for part in msg['payload']['parts']:
            if part['mimeType'] == 'text/plain' and 'data' in part['body']:
                return base64.urlsafe_b64decode(part['body']['data']).decode('utf-8')
    return None

def main():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    try:
        service = build('gmail', 'v1', credentials=creds)
        random_chars = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        temp_email = BASE_EMAIL.replace("@", f"+{random_chars}@")

        print(f"Temporary email created: {temp_email}")

        while True:
            results = service.users().messages().list(userId='me', maxResults=1, q=f"to:{temp_email}").execute()
            messages = results.get('messages', [])

            if not messages:
                print("No new emails yet...")
                time.sleep(10) 
                continue

            msg = service.users().messages().get(userId='me', id=messages[0]['id']).execute()
            email_content = get_email_content(msg)
            if email_content:
                print(f"Email received:\n{email_content}")
            else:
                print("Failed to extract email content.")
            break

    except HttpError as error:
        print(f'An error occurred: {error}')

if __name__ == '__main__':
    main()
