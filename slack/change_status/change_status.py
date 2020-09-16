import json
import os
import requests
import subprocess

user_id = os.environ['CMT_SLACK_USER_ID']
cmt_bssid = os.environ['CMT_BSSID']
token = 'xoxp-462861973812-563395089110-1257868706036-6ee8c557475799ff6f0a7cc559412d03'
headers = {'Authorization': 'Bearer %s' % token, 'X-Slack-User': user_id, 'Content-Type': 'application/json; charset=utf-8'}
slack_url = 'https://slack.com/api/users.profile.set'

cmd = '/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I | grep BSSID | awk \'{print $2}\''
current_bssid = (subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]).decode('utf-8')

def post_slack_status(current_bssid):
    if cmt_bssid == current_bssid:
        payload = {'profile': {'status_emoji': ':pencil:', 'status_text': '研究室'}}
    else:
        payload = {'profile': {'status_emoji': ':house:', 'status_text': '自宅'}}
    res = requests.post(slack_url, data=json.dumps(payload), headers=headers).json()

post_slack_status(current_bssid[:-1])
