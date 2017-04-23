#!/usr/bin/env python

import boto3
import json

bucket = boto3.resource('s3').Bucket('fmaj7-tennis-button')
secret_key = 'poppyseed.json'

def get_secrets():
    for obj in bucket.objects.all():
        if secret_key == obj.key:
            return json.loads(obj.get()['Body'].read())

if __name__ == '__main__':
    secrets = get_secrets()

    keys = ['group-id', 'payer-id', 'debtor-id', 'csrf-token', 'user-credentials', 'splitwise-session']
    new_secrets = {}
    for key in keys:
        default = secrets.get(key, None)
        value = raw_input('{} [{}]: '.format(key, default))
        new_secrets[key] = value or default

    print "\nUpdating Secrets..."
    bucket.put_object(Key=secret_key, Body=json.dumps(new_secrets))

    print "\nNew Scerets: \n{}".format(json.dumps(get_secrets(), sort_keys=True, indent=4))
