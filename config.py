import os

# app configs
# opsgenie
opsgenie_api_key = os.environ["OPSGENIE_API_KEY"]
cloudops_schedule_id = os.environ.get("CLOUDOPS_SCHEDULE_ID")
# slack
tomorrow_workflow = os.environ.get("TOMORROW_WORKFLOW")
today_workflow = os.environ.get("TODAY_WORKFLOW")
