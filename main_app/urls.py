"""main_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', 'admin.site.urls'),
    path('api/<str:version>/', include([
        path('example_app/', include(('apps.example_app.api.urls', 'example_app'),
                                     namespace='example_app')),
    ])),
]

if settings.ENABLE_PROMETHEUS:
    urlpatterns += [
        path('', include('django_prometheus.urls')),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG and 'silk' in settings.INSTALLED_APPS:
    urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
