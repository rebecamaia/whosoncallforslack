import requests
import config
import datetime
import pytz

base_api_url = "https://api.opsgenie.com/v2/"
opsgenie_api_key = config.opsgenie_api_key

def opsgenie_who_is_oncall(schedule_id, date):
    if date == 'today':
        url = "%sschedules/%s/on-calls" % (base_api_url, schedule_id)
    elif date == 'tomorrow':
        tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
        timezone = pytz.timezone("Brazil/DeNoronha")
        date = datetime.datetime(tomorrow.year, tomorrow.month, tomorrow.day, 11, 0, 0, 0, timezone)
        url = "%sschedules/%s/on-calls?date=%s" % (base_api_url, schedule_id, date.isoformat())

    print("Processing URL: " + url)

    headers = {"Authorization": "GenieKey %s" % (opsgenie_api_key)}
    response = requests.get(url, headers=headers)
    print("Processing response...")
    print(response.status_code)
    print(response.json())
    if response.json().get('data').get('onCallParticipants'):
        oncall_email = response.json()["data"]["onCallParticipants"][0]["name"]
    else:
        oncall_email = "No one is on support!"
    return oncall_email
