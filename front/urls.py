from django.urls import path

from .views import IndexPageView, AboutPageView, ContactPageView, ToolsPageView

app_name = 'front'
urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('tools/', ToolsPageView.as_view(), name='tools'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
]