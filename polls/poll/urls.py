from django.urls import path
from . import views

# 네임 스페이스(이름 공간) - 소속이라고 보면 돼요
app_name = 'poll'

urlpatterns = [
    #http://127.0.0.1:8000/poll/
    path("", views.poll_list, name='poll_list'),    # views.index에서 poll_list로 수정하였음
    #http://127.0.0.1:8000/poll/1
    path("<int:question_id>/", views.detail, name='detail'),
    #http://127.0.0.1:8000/poll/1/vote
    path("<int:question_id>/vote/", views.vote, name='vote'),
    #http://127.0.0.1:8000/poll/test/
    path("test/", views.test),
]