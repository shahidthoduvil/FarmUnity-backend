from django.urls import path
from .views import *
from .views2 import *

urlpatterns = [
 
    path('questions/', QuestionListView.as_view(), name='question-list'),
    path('<int:question_id>/solutions/', SolutionListView.as_view(), name='solution-list'),
    path('create-questions/', CreateQuestionView.as_view()),
    path('create-solutions/', CreateAnswerView.as_view()),
    path('<int:question_id>/question-delete/', DeleteQuestionView.as_view()),
    path('solution-delete/<int:solution_id>/', DeleteSolutionView.as_view()),
    path('admin-notifications/<int:user_id>/', NotificationListView.as_view()),
    path('user-notifications/',UserNotificationListView.as_view()), 
    path('send-notifications/',AdminNotificationCreateView.as_view()),
    path('delete-notification/<int:id>/', DeleteNotificationAPIView.as_view()),
    path("user-previous-chats/<int:user1>/<int:user2>/", PreviousMessagesView.as_view()),
    path('cached-news/', CachedNewsListView.as_view(), name='cached-news-list'),
    path('fetch-initial-news/', FetchAndStoreInitialNews.as_view(), name='fetch-initial-news'),



]


