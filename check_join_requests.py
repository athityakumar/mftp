# def check_join_requests(users):
#     leprechaun_authenticated_emails = connect_to_leprechaun_db()
#     for user in users:
#         email_id = user.email_id()
#         if email_id in leprechaun_authenticated_emails:
#             # Accept this user's join request with directory API

# if __name__ == "__main__":
#     users = # From the directory API
#     for user in requesting_users:
#         if 
#         check_join_request_of()

from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import pprint
import json

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/groupssettings-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/admin.directory.group'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'MFTP'

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'groupssettings-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """Shows basic usage of the Google Admin-SDK Groups Settings API.

    Creates a Google Admin-SDK Groups Settings API service object and outputs a
    group's settings identified by the group's email address.
    """
    credentials = get_credentials()
    # http = credentials.authorize(httplib2.Http(proxy_info=httplib2.ProxyInfo(httplib2.socks.PROXY_TYPE_HTTP_NO_TUNNEL, '172.16.2.30', 8080, proxy_user='', proxy_pass='')))
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('groupssettings', 'v1', http=http)
    # service = discovery.build(serviceName='admin', version='directory_v1', http=http)

    # groupEmail = \
    #     raw_input('Enter the email address of a Google Group in your domain: ')

    'https://www.googleapis.com/admin/directory/v1/groups/groupKey'

    groupEmail = 'kgp-tnp-noticeboard'
    # groupEmail = 'kgp-tnp-noticeboard@googlegroups.com'

    print('Service name:', service.groups())
    try:
        results = service.groups().get(groupUniqueId=groupEmail).execute()
        print(json.dumps(results, indent=4))
    except:
        print('Unable to read group: {0}'.format(groupEmail))
        raise

def get_group_members(group):
    url = 'https://www.googleapis.com/admin/directory/v1/groups/{}/members'.format(group)
    return call_google_api("GET", url)

# def remove_group_member(group, member):
#     url = 'https://www.googleapis.com/admin/directory/v1/groups/{}/members/{}'.format(group, member)
#     return call_google_api("DELETE", url)    


def add_group_member(group, payload=False):
    url = 'https://www.googleapis.com/admin/directory/v1/groups/{}/members'.format(group)
    return call_google_api("POST", url, payload)


def call_google_api(method, url, payload=False):
    content = {}
    try:
        print(method, url)
        http = get_conn()
        print(http)
        if payload:
            (resp, content) = http.request(uri=url, method=method, body=json.dumps(payload))
        else:
            print('Trying...')
            (resp, content) = http.request(uri=url, method=method)
            print(resp, content)
    except Exception as e:
        print("Failed to post request to [{}] due to: {}".format(url, e))
    return json.loads(content)

def get_conn():
    credentials = get_credentials()
    http = httplib2.Http(proxy_info=httplib2.ProxyInfo(httplib2.socks.PROXY_TYPE_HTTP, '172.16.2.30', 8080, proxy_user=None, proxy_pass=None))
    return(credentials.authorize(http))

def main2():
    res = get_group_members('kgp-tnp-noticeboard@googlegroups.com')
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(res)

if __name__ == '__main__':
    main2()

# import os
# import pprint

# import google.oauth2.credentials

# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError
# from google_auth_oauthlib.flow import InstalledAppFlow

# pp = pprint.PrettyPrinter(indent=2)

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret.
# CLIENT_SECRETS_FILE = "client_secret.json"

# This access scope grants read-only access to the authenticated user's Drive
# account.
# SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
# API_SERVICE_NAME = 'drive'
# API_VERSION = 'v3'

# def get_authenticated_service():
#   flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
#   credentials = flow.run_console()
#   return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

# def list_drive_files(service, **kwargs):
#   results = service.files().list(
#     **kwargs
#   ).execute()

#   pp.pprint(results)

# if __name__ == '__main__':
#   # When running locally, disable OAuthlib's HTTPs verification. When
#   # running in production *do not* leave this option enabled.
#   os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
#   service = get_authenticated_service()
#   list_drive_files(service,
#                    orderBy='modifiedByMeTime desc',
#                    pageSize=5)
