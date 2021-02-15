def create_label(label_name, service, mlv="show", llv="labelShow"):
    def existing_labels():
        existing_label_names = []

        list_labels = service.users().labels().list(userId="me").execute()
        get_labels = list_labels.get('labels', [])
        for label in get_labels:
            existing_label_names.append(label['name'])

        if label_name not in existing_label_names:
            label = {
                "messageListVisibility": mlv,
                "labelListVisibility": llv,
                "name": label_name
            }
            return label
        else:
            return None

    result = existing_labels()  # check if label_name already exists

    try:  # try create new label
        if result is not None:
            create_new_label = service.users().labels().create(userId="me", body=result).execute()
            print(f'\nLabel "{label_name}" created.')
        else:
            print(f'\nLabel "{label_name}" already exists.')
    except Exception as e:
        print(f'Unexpected Error: {e}')
        exit()
