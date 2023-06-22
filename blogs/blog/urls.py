from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:post_id>/', views.detail, name='detail'),    # 상세 페이지
    path('post/create/', views.post_create, name='post_create'),
]