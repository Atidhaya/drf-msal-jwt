from django.conf import settings
from rest_framework.settings import APISettings

USER_SETTINGS = getattr(settings, 'DRF_MSAL', None)

DEFAULTS = {
    'MSAL_CLIENT_ID': None,
    'MSAL_CLIENT_SECRET': None,
    'MSAL_AUTHORITY_URL': 'https://login.microsoftonline.com/common/',
    'MSAL_REDIRECT_URL': None,
    'MSAL_OPENID_CONFIG': 'https://login.microsoftonline.com/common/v2.0/.well-known/openid-configuration',
    'MSAL_SCOPES': ["User.ReadBasic.All"]
}

IMPORT_STRINGS = None

api_settings = APISettings(USER_SETTINGS, DEFAULTS, IMPORT_STRINGS)
