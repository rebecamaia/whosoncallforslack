import json
import requests


def get_request_data(user_cloudops):
    raw_data = {
        "user_cloudops": user_cloudops
    }
    return json.dumps(raw_data)


def send_info_to_slack(workflow, user_cloudops):
    print("Sending info to slack...")
    status = requests.post(workflow, data=get_request_data(user_cloudops))
    print(status.status_code)
    print(status.text)