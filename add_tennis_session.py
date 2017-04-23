#!/usr/bin/env python

import requests
from datetime import *
from dateutil.tz import *
import boto3
import json

bucket = boto3.resource('s3').Bucket('fmaj7-tennis-button')

def handler(event, context):
    try:
        import requests.packages.urllib3
        requests.packages.urllib3.disable_warnings()
    except:
        pass

    secrets = {}
    for obj in bucket.objects.all():
        if 'poppyseed.json' == obj.key:
            secrets = json.loads(obj.get()['Body'].read())

    now = datetime.now(tzlocal()).strftime("%a %b %d %Y %H:%M:%S GMT%z (%Z)")
    r = requests.post('https://secure.splitwise.com/api/v3.0/create_expense',
            data = {
                'cost':25,
                'currency_code':'USD',
                'group_id': secrets['group-id'],
                'users__0__user_id': secrets['debtor-id'],
                'users__0__paid_share':0.00,
                'users__0__owed_share':12.50,
                'users__1__user_id': secrets['payer-id'],
                'users__1__paid_share':25.00,
                'users__1__owed_share':12.50,
                'category_id':18,
                'date': now,
                'description': "Tennis Bill Bot - " + now,
                'creation_method':'equal',
            },
            headers = {
                'X-CSRF-Token': secrets['csrf-token'],
                'Content-Type': 'application/x-www-form-urlencoded',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko)'
                        + ' Chrome/57.0.2987.133 Safari/537.36',
            },
            cookies = {
                'user_credentials': secrets['user-credentials'],
                '_splitwise_session': secrets['splitwise-session'],
            },
        )
    print("Response:\n{}".format(json.dumps(json.loads(r.text), indent=2)))

if __name__ == "__main__":
    handler(None, None)
