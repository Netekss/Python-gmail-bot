def label_id(service, label_name):
    all_labels = service.users().labels().list(userId="me").execute()
    get_labels = all_labels.get('labels', [])

    expected_id = ''

    for label in get_labels:
        if label['name'] == label_name:
            expected_id += label['id']

    return expected_id
