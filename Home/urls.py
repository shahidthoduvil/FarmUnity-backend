from django.contrib import admin

from django.urls import path
from .import views



urlpatterns = [
    path('banner-list/',views.getBannerLIst.as_view()),
    path('quote-list/',views.getQuoteLIst.as_view()),
    path('member-list/',views.getMemberLIst.as_view()),
    

]
