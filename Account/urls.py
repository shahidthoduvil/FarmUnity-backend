from django.urls import path
from .views import RegisterView
from .import views
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)

urlpatterns = [
    path('', views.getRoutes), 
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('google_authentication/',views.GoogleAuthentication.as_view()),
    path('register/',RegisterView.as_view()),
    path('activate/<uidb64>/<token> ', views.Activate, name='activate'),


    path('forgot_password/', views.ForgotPasswordView.as_view(), name='forgot_password'),
    path('resetPassword_validate/<uidb64>/<token>/',views.ResetPassword_validate,name='resetPassword_validate'),
    path('resetPassword/',views.ResetPasswordView.as_view(), name='reset_password'),
 
 # admin side

    
    path('blockUser/<int:id>/',views.BlockUser.as_view(),name="blockUser") ,


#  # user Details

   path('getuserdetails/<int:user_id>',views.GetUserDetails.as_view(),name='UserDetails'),


]

