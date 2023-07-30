from rest_framework.permissions import BasePermission
from .helpers import decode_jwt_payload
import json
from .models import User


def authenticate_request(request):
    auth_header = request.headers.get('Authorization')
    try:
        role = json.loads(request.body.decode('utf-8')).get('role')
    except:
        pass

    if not auth_header:
        return None

    if not auth_header.startswith('Bearer '):
        return None

    token = auth_header.split(' ')[1]
    decoded_payload = decode_jwt_payload(json.loads(token).get('access'))

    if decoded_payload:
        user_id = decoded_payload.get('user_id')
        try:
            user = User.objects.get(id=user_id)
            return True
        except:
            return None
    else:
        return None



class IsAuthenticatedWithToken(BasePermission):
    def has_permission(self, request, view):
        jwt_payload = authenticate_request(request)
        return jwt_payload is not None