

from django.contrib import admin
from django.urls import path
from pack_login.views import wellcome

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', wellcome),
]
