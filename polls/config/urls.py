from django.contrib import admin
from django.urls import path, include

from poll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('poll/', include('poll.urls')),     # views 에러줄 뜨면 import - views.py에서

]
