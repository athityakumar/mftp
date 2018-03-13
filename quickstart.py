import google.oauth2.credentials

credentials = google.oauth2.credentials.Credentials(
    "998260994591-nn2aldbrjtt2ha52fhnjrfigjqks8hsq.apps.googleusercontent.com",
    "EyEJR6tsgevGeWG6-4C0sd9q",
    'https://www.googleapis.com/auth/apps.groups.settings')

from google.auth.transport.requests import AuthorizedSession

authed_session = AuthorizedSession(credentials)
response = authed_session.get(
    'https://www.googleapis.com/storage/v1/b')
