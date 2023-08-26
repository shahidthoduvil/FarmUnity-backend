from django.contrib import admin

from django.urls import path
from .import views
from .import views2



urlpatterns = [
    path('banner-list/',views.getBannerLIst.as_view()),
    path('Admin-banner/',views.getAdminBannerLIst.as_view()),
    path('banner/<int:pk>/list_unlist/',views.ListUnlistBanner.as_view()),
    path('banner/delete/<int:pk>/',views.bannerDelete),
    path('banner/add/',views.BannerCreateView.as_view()),
    path('banner/<int:pk>/Edit',views.BannerEditView.as_view()),

    path('quote-list/',views.getQuoteLIst.as_view()),
    path('Admin-quote/',views.getAdminquote.as_view()),
    path('quote/delete/<int:pk>/',views.quoteDelete),
    path('quote/add/',views.QuoteCreateView.as_view()),
    path('quote/<int:pk>/list_unlist/',views.ListUnlist.as_view()),
    path('quote/update/<int:pk>/',views.QuoteUpdate.as_view()),


   
    path('member-list/',views.getMemberLIst.as_view()),
    path('member/<int:pk>/list_unlist/',views.ListUnlistMember.as_view()),
    path('Admin-member/',views.getAdminMember.as_view()),
    path('member/delete/<int:pk>/',views.memberDelete),
    path('member/add/',views.MemberCreateView.as_view()),
    path('member/<int:pk>/Edit/',views.MemberEditView.as_view()),


   path('users/category/<str:categoryName>/', views2.UserByCategoryView.as_view(), name='users-by-category'),
   path('users/search/<str:categoryName>/', views2.SearchUsersByCategory.as_view(), name='search-users-by-category'),
   path('users/auto-suggest/<str:categoryName>/', views2.AutoSuggestUsers.as_view(), name='auto-suggest'), 
   path('getuserinfo/<str:username>/',views2.GetUserinfo.as_view(),name='UserDetails'),


# path('reviews/', views2.AllReviewsListView.as_view()),

   path('<int:user1_id>/reviews/', views2.User1ReviewsListView.as_view()),
   path('<str:username>/singlereview/', views2.User1Reviews.as_view()),

   path('create-review/', views2.User1CreateReviews.as_view(), name='user1-reviews'),

    path('<int:id>/delete-review/', views2.ReviewDeleteView.as_view()),



]

