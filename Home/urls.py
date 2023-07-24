from django.contrib import admin

from django.urls import path
from .import views



urlpatterns = [
    path('banner-list/',views.getBannerLIst.as_view()),
    path('banner/delete/<int:pk>/',views.bannerDelete),
    path('banner/add/',views.BannerCreateView.as_view()),

    path('quote-list/',views.getQuoteLIst.as_view()),
    path('quote/delete/<int:pk>/',views.quoteDelete),
    path('quote/add/',views.QuoteCreateView.as_view()),
    path('quote/update/<int:pk>/',views.QuoteUpdate.as_view()),


   
    path('member-list/',views.getMemberLIst.as_view()),
    path('member/delete/<int:pk>/',views.memberDelete),
    path('member/add/',views.MemberCreateView.as_view())

    

]

