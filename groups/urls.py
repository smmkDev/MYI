from django.urls import path

from .views import *
from .api_views import *


urlpatterns = [
   path('post/add/<int:pk>', AddPostView.as_view(), name="add_post"),
   path('api/post/detail/<int:pk>', PostDetailApiView.as_view()),
   path('post/detail/<int:pk>', PostDetailView.as_view()),
   path('api/group', GroupCreateApiView.as_view()),
   path('group', GroupCreateView.as_view()),
   path('group/detail/<int:pk>', GroupDetailView.as_view(), name="group_detail"),
   path('api/group/detail/<int:pk>', GroupDetailApiView.as_view()),
   path('api/group/list', GroupListApiView.as_view()),
   path('group/list', GroupListView.as_view()),
   path('ans/add/<int:pk>', AddAnswerView.as_view(), name="add_ans"),
   path('join/<int:pk>', JoinGroupView.as_view()),
]