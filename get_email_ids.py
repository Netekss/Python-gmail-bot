def email_ids(service, searching):
    def get_messages_ids():
        messages_ids = []

        all_messages = service.users().messages().list(userId="me").execute()
        get_messages = all_messages.get('messages', [])

        for message_id in get_messages:
            messages_ids.append(message_id['id'])

        return messages_ids

    def get_specific_ids(ids):
        expected_messages = []

        for message_id in ids:
            current_message = service.users().messages().get(userId="me", id=message_id).execute()
            message_content = current_message['payload']['headers']

            for content in message_content:
                if searching in content['value']:
                    if content['name'] == 'From':
                        mail_sender = content['value'].split('<')[0].replace('"', '').lower()
                        if 'no-reply' in mail_sender:
                            pass
                        else:
                            mail_sender = mail_sender.rstrip(' ')
                            mail_sender = mail_sender.lstrip(' ')
                            if mail_sender == searching.lower():
                                expected_messages.append(message_id)

        return expected_messages

    ids = get_messages_ids()
    expected_ids = get_specific_ids(ids)

    return expected_ids
