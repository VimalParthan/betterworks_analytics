from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('department.urls')),
    path('', include('user.urls')),
    path('', include('objective.urls')),
    path('', include('team.urls')),
    path('', include('key_result.urls')),
]
