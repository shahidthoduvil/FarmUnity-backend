import base64
import json 
from rest_framework.permissions import BasePermission
from django.contrib.auth import get_user_model
import json
from .models import User

User = get_user_model()

def decode_jwt_payload(token):
    try:
        _, payload_base64, _ = token.split('.')
        payload_bytes = base64.urlsafe_b64decode(payload_base64 + '==')
        payload_json = payload_bytes.decode('utf-8')
        return json.loads(payload_json)
    except ValueError:
        return None


def authenticate_user(request,role):

    auth_header=request.headers.get('Authorization')
    
    print(auth_header)
    if not auth_header:
        return None
    
    if not auth_header.startswith('Bearer'):
        return None
    

    token=auth_header.split(' ')[1]
    decoded_payload=decode_jwt_payload(json.loads(token).get('access'))
    if decoded_payload:
        user_id=decoded_payload.get('user_id')
        try:
            user=User.objects.get(id=user_id)
        except Exception as e:
            return None

        if role=='user':
            return True
        elif role=='admin':
            return True
        else:
            return None
    return None

        
 