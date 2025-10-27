# social_media_api/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include accounts app URLs under the 'api/auth/' prefix
    path('api/auth/', include('accounts.urls')),
]