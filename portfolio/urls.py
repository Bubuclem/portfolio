'''
portfolio URL Configuration
'''
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('',include('profil.urls')),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('next/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
]

handler404 = 'portfolio.views.handler404'
handler500 = 'portfolio.views.handler500'
