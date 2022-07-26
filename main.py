import config
import opsgenie_helper
import slack_helper
import sys


def who_is_on_call(workflow, date):
    print("Checking who is on call....")
    user_cloudops = opsgenie_helper.opsgenie_who_is_oncall(config.observabilityservices_schedule_id, date)
    print("Done checking who is on call.... \CloudOps: " + user_cloudops)
    slack_helper.send_info_to_slack(workflow, user_cloudops)


if __name__ == "__main__":
    date = sys.argv[1]
    if date == "tomorrow":
        who_is_on_call(config.tomorrow_workflow, date)
    elif date == "today":
        who_is_on_call(config.today_workflow, date)
    else:
        print("Please specify a date: tomorrow or today")
