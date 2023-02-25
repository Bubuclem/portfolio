from django.urls import path

from profil.views import ProfilView

app_name = 'profil'
urlpatterns = [
    path('', ProfilView.as_view(), name='profil'),
]