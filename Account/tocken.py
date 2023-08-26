from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model


User = get_user_model()

def create_jwt_pair_tokens(user: User):
    refresh = RefreshToken.for_user(user)
    refresh['is_setup_complete'] = user.is_setup_complete
    tokens = {
        "access": str(refresh.access_token),
        "refresh": str(refresh)
    }
    return tokens


