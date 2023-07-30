import base64
import json 
from rest_framework.permissions import BasePermission

import json
from .models import User


def decode_jwt_payload(token):
    try:
        _, payload_base64, _ = token.split('.')
        payload_bytes = base64.urlsafe_b64decode(payload_base64 + '==')
        payload_json = payload_bytes.decode('utf-8')
        return json.loads(payload_json)
    except ValueError:
        return None
