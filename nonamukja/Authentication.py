from django.conf import settings
from rest_framework import authentication, exceptions
from rest_framework.authentication import get_authorization_header
from accounts.models import User
import jwt

class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        try:
            token = get_authorization_header(request).decode('utf-8')
            if token is None or token == "null" or token.strip() == "":
                raise exceptions.AuthenticationFailed('Authorization Header or Token is missing on Request Headers')
            print(token)
            decoded = jwt.decode(token, settings.JWT_SECRET_KEY)
            username = decoded['email']
            user_obj = User.objects.get(email=email)
        except jwt.ExpiredSignature :
            raise exceptions.AuthenticationFailed('Token Expired, Please Login')
        except jwt.DecodeError :
            raise exceptions.AuthenticationFailed('Token Modified by thirdparty')
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed('Invalid Token')
        except Exception as e:
            raise exceptions.AuthenticationFailed(e)
        return (user_obj, None)

    def get_user(self, userid):
        try:
            return User.objects.get(pk=userid)
        except Exception as e:
            return None
