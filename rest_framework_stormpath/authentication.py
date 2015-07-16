import jwt
import base64
import requests
from time import time
from django.conf import settings
from django.core.cache import cache
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import (BaseAuthentication,
                                           get_authorization_header)


class StormpathAuthentication(BaseAuthentication):
    def authenticate(self, request):
	try:
	    (scheme, token) = get_authorization_header(request).split()
	except:
	    return None

        try:
            payload = jwt.decode(token, verify=False)
	    jti = payload.get('jti')
        except jwt.InvalidTokenError:
	    self._fail('Invalid token.')
	except:
	    self._fail()

	user = cache.get(jti)
	if user:
	    return (user, jti)

	if not self._validate_token(token):
	    self._fail('Invalid credentials.')

	user = self._get_user(payload)
	return (user, token)

    def _validate_token(self, token):
	url = "{0}/authTokens/{1}".format(settings.STORMPATH_APPLICATION, token)
	resp = requests.get(url, headers=self._get_headers(), allow_redirects=False)
	return True if resp.status_code == 302 else None

    def _get_user(self, payload):
	try:
	    jti = payload.get('jti')
	    resp = requests.get(
		"{}?expand=customData".format(payload.get('sub')),
		headers=self._get_headers())
	    data = resp.json()
	    user = User()
	    user.username = data.get('username')
	    user.first_name = data.get('givenName')
	    user.last_name = data.get('surname')
	    user.email = data.get('email')
	    user.customData = data.get('customData')
	    #user.created  = data.get('createdAt')
	except:
	    return None

	cache.set(jti, user, payload.get('exp') - time())
	return user

    def _get_headers(self):
	key = "{0}:{1}".format(settings.STORMPATH_ID, settings.STORMPATH_SECRET)
	return {'Authorization': 'Basic {}'.format(base64.b64encode(key))}
	
    def _fail(self, msg=None):
	raise AuthenticationFailed(msg)

