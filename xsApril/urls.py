from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.http import HttpResponse
from .views import HelloView

urlpatterns = [
                  path('', HelloView.as_view()),
                  path('admin/', admin.site.urls),
                  path('api-auth/', include('rest_framework.urls')),
                  path('api/v1/', include('rofl.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
