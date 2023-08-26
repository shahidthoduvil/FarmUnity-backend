from django.urls import path
from .views import RegisterView
from .import views
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
from .import views2
urlpatterns = [
    path('', views.getRoutes), 
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('google_authentication/',views.GoogleAuthentication.as_view()),
    path('register/',RegisterView.as_view()),
    path('activate/<uidb64>/<token> ', views.Activate, name='activate'),
    path('is-user/',views2.is_user),
    path('is-admin/',views2.is_admin),

    path('forgot_password/', views.ForgotPasswordView.as_view(), name='forgot_password'),
    path('resetPassword_validate/<uidb64>/<token>/',views.ResetPassword_validate,name='resetPassword_validate'),
    path('resetPassword/',views.ResetPasswordView.as_view(), name='reset_password'),
 
 # admin side    
    path('blockUser/<int:id>/',views.BlockUser.as_view(),name="blockUser") ,
    path('listUser/', views.ListUserview.as_view()),
    path('adminsearchUser/', views.AdminSearchUser.as_view()),


#  # user Details

   path('getuserdetails/<int:user_id>/',views.GetUserDetails.as_view(),name='UserDetails'),
   path('getsingledetails/<int:user_id>/',views.GetUserDetails.as_view(),name='UserDetails'),
   path('profile-setup1/<int:id>/', views.userProfileSet1.as_view()),
   path('profile-setup2/', views.userProfileSet2.as_view()),
    path('update-profile/<int:id>/', views2.UserProfileUpdateView.as_view(), name='update-profile'),
   path('category-occupation-list/', views2.CategoryOccupationListView.as_view(), name='category-occupation-list'),
   path('update_address/<int:user__id>/', views2.AddressUpdateView.as_view(), name='update-address'),
   path('check-profile-setup/<int:id>/', views2.check_profile_setup, name='check_profile_setup'),
   path('get-new-token', views.get_new_token),
   path('admin-profiles/<int:user_id>/', views2.AdminProfileDetailView.as_view()),
]