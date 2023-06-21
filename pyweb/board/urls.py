from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('<int:question_id>/', views.detial, name='detail'),
    path('question/create/', views.question_create, name='question_create'),
    # 질문 하나에는 답변 여러개 남길 수 있어야 하죠! <int:question_id>/
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),    # 답변 등록
    path('question/delete/<int:question_id>/', views.question_delete,
         name='question_delete'),   # 질문 삭제
]