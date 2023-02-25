'''
Views for back app
'''
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView, ListView, FormView

from back.models import User
from front.models import Message, Newsletter
from back.forms import ProfilForm, UserForm

BASE_TEMPLATE = 'pages/back/{page}.html'

class LoginRequired(LoginRequiredMixin):
    '''
    Login required mixin
    '''
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

class IndexPageView(LoginRequired, TemplateView):
    ''' 
    Index Page 
    '''
    template_name = BASE_TEMPLATE.format(page='index')
    success_url = 'back:index'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['datetime'] = datetime.now().time()
        context['messages'] = Message.objects.all().order_by('-date_created')[:3]
        context['newsletters'] = Newsletter.objects.all().order_by('-date_created')[:5]
        return context

class UsersPageView(LoginRequired, ListView):
    ''' 
    Users Page 
    '''
    template_name = BASE_TEMPLATE.format(page='users')
    model = User
    paginate_by = 10
    context_object_name = 'users'
    success_url = 'back:users'

    def get_queryset(self):
        return User.objects.all().order_by('first_name')

class UserPageView(LoginRequired, FormView):
    ''' 
    User Page 
    '''
    template_name = BASE_TEMPLATE.format(page='user')
    form_class = UserForm
    success_url = 'back:user'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['form'] = UserForm(instance=User.objects.get(pk=self.kwargs['pk']))
        return context

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST, instance=User.objects.get(pk=self.kwargs['pk']))
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        return self.form_invalid(form)

class NewsletterPageView(LoginRequired, ListView):
    ''' 
    Newsletter Page 
    Get all newsletter from database
    '''
    template_name = BASE_TEMPLATE.format(page='newsletters')
    model = Newsletter
    paginate_by = 10
    context_object_name = 'newsletters'
    success_url = 'back:newsletters'

    def get_queryset(self):
        return Newsletter.objects.all().order_by('email')

class MessagePageView(LoginRequired, TemplateView):
    ''' 
    Message Page 
    Get messages from database
    '''
    template_name = BASE_TEMPLATE.format(page='message')
    success_url = 'back:message'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = Message.objects.get(id=kwargs['id'])
        return context

class MessagesPageView(LoginRequired, ListView):
    ''' List of all messages
    '''
    template_name = BASE_TEMPLATE.format(page='messages')
    model = Message
    paginate_by = 10
    context_object_name = 'messages'
    success_url = 'back:messages'

    def get_queryset(self):
        return Message.objects.all().order_by('-date_created')

class ProfilePageView(LoginRequired, FormView):
    ''' 
    Profile Page 
    '''
    template_name = BASE_TEMPLATE.format(page='profile')
    form_class = ProfilForm
    success_url = 'back:profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProfilForm(instance=User.objects.get(id=self.request.user.id))
        return context

    def post(self, request, *args, **kwargs):
        form = ProfilForm(request.POST, request.FILES,
        instance=User.objects.get(id=self.request.user.id))
        if form.is_valid():
            form.save()
            return self.form_valid(form)

        context = self.form_invalid(form)
        return context

class LoginPageView(AuthenticationForm, TemplateView):
    '''
    Login page
    '''
    template_name = 'registration/login.html'
    form_class = AuthenticationForm

class LogoutPageView(TemplateView):
    '''Logout page'''
    template_name = BASE_TEMPLATE.format(page='logout')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)
