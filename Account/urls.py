from django.urls import path
from .views import RegisterView
from.import views
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)

urlpatterns = [
    path('', views.getRoutes), 
    path('register/',RegisterView.as_view()),
    path('activate/<uidb64>/<token> ', views.Activate, name='activate'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
