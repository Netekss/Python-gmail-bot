def add_to_label(service, message_id, label_id):

    body = {
        "addLabelIds": [
            label_id
        ],
        "removeLabelIds": []
    }

    try:
        service.users().messages().modify(userId="me", id=message_id, body=body).execute()
        print(f'message (id {message_id}) => has been added')
    except Exception as error:
        print(f'Unexpected error: {error}')
        exit()
