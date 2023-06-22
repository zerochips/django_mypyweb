from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),  # http://127.0.0.1:8000/    # 첫 페이지 - 루트 경로
    path('blog/', include('blog.urls')),
]

urlpatterns += static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT)   # 인수가 두 개 들어갑니다
