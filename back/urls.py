from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import IndexPageView, UsersPageView, MessagePageView, MessagesPageView, NewsletterPageView, ProfilePageView, LoginPageView

app_name = 'back'
urlpatterns = [
    path('', 
    login_required(IndexPageView.as_view()), 
    name='index'),

    path('users/',
    login_required(UsersPageView.as_view()),
    name='users'),

    path('newsletters/',
    login_required(NewsletterPageView.as_view()),
    name='newsletters'),

    path('message/<int:id>/',
    login_required(MessagePageView.as_view()),
    name='message'),

    path('messages/',
    login_required(MessagesPageView.as_view()),
    name='messages'),

    path('profile/',
    login_required(ProfilePageView.as_view()),
    name='profile'),

    path('login/',
    LoginPageView.as_view(),
    name='login'),
]