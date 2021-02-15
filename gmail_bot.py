import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from create_new_label import create_label
from get_label_id import label_id
from get_email_ids import email_ids
from add_email_to_label import add_to_label

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly',
          'https://www.googleapis.com/auth/gmail.labels',
          'https://www.googleapis.com/auth/gmail.modify']


def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    credentials = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            credentials = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            credentials = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(credentials, token)

    # Make the API request
    service = build('gmail', 'v1', credentials=credentials)

    # My content
    label_name = input('\nInput label name: ')
    sender = input('Input expected sender: ')

    #  == run ==
    try:
        # 1 create new label
        label = create_label(label_name, service)  # <-- creating new label
        print('\n=== processing ===')
        print('=== please wait ===')

        # 2 get label id
        id_label = label_id(service, label_name)  # <-- returning label id

        # 3 get messages with expected sender
        messages_to_add = email_ids(service, sender)  # <-- returning messages ids with expected sender

        # 4 add messages into label
        if len(messages_to_add) != 0:
            for message_id in messages_to_add:
                add_to_label(service, message_id, id_label)
        else:
            print(f"\nCan't find any message with sender: {sender}")
    except Exception as error:
        print(f'Unexpected error: {error}')


if __name__ == '__main__':
    main()
