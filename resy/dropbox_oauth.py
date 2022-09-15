#!/usr/bin/env python3

import dropbox
from dropbox import DropboxOAuth2FlowNoRedirect

'''
This example walks through a basic oauth flow using the existing long-lived token type
Populate your app key and app secret in order to run this locally
'''
APP_KEY = "yjgk8ag77s15s92"
APP_SECRET = "24k50g99szjgbqx"
authorization_code = 'yjgk8ag77s15s92'

auth_flow = DropboxOAuth2FlowNoRedirect(APP_KEY, APP_SECRET)

authorize_url = auth_flow.start()
print("1. Go to: " + authorize_url)
print("2. Click \"Allow\" (you might have to log in first).")
print("3. Copy the authorization code.")
auth_code = input("Enter the authorization code here: ").strip()

try:
    oauth_result = auth_flow.finish(auth_code)
except Exception as e:
    print('Error: %s' % (e,))
    exit(1)

with dropbox.Dropbox(oauth2_access_token=oauth_result.access_token) as dbx:
    dbx.users_get_current_account()
    print("Successfully set up client!")


curl -u yjgk8ag77s15s92:24k50g99szjgbqx \
-d "code=6yxBtc4dZJAAAAAAAAAFBpIladVg-PAidp0jBqPmZCY&grant_type=authorization_code" \
-H "Content-Type: application/x-www-form-urlencoded" \
-X POST "https://api.dropboxapi.com/oauth2/token"