from django.urls import path
from .views import *
from .views2 import *

urlpatterns = [
 
    path('posts/<int:user_id>/',PostList.as_view()),
    path('post/<int:user_id>/',PostListAdmin.as_view()),
    path('add-post/', AddPostView.as_view(), name='add-post'),
    path('delete/<int:id>/', DeletePostView.as_view(), name='delete-post'),
    path('<int:post_id>/user-comments/', UserCommentsView.as_view(), name='user_comments'),
    path('<int:post_id>/comments/', PostCommentsView.as_view(), name='post_comments'),
    path('add-comment/', AddCommentView.as_view(), name='add-comment'),
    path('user-posts/<int:user_id>/', UserPostList.as_view()),
    path('user-posts/<str:username>/', UserPost.as_view()),
    path('Postdelete/<int:post_id>/', DeletePost.as_view(), name='delete-post'),
    path('delete-comment/<int:id>/',  CommentDeleteView.as_view(), name='delete_comment'),
    path("like-post/",PostLikeView.as_view()),
    path("un-like-post/<int:post_id>/<int:user_id>/",un_like_post),
    path("follow/<int:user1>/<int:user2>/", FollowView.as_view()),


]



