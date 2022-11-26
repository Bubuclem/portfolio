from datetime import datetime
from django.urls import reverse
from django.views.generic import TemplateView, ListView, FormView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from back.forms import LoginForm, ProfilForm, UserForm
from back.models import User
from front.models import Message, Newsletter

BASE_TEMPLATE = 'pages/back/{page}.html'
SUCCESS_URL = '/dashboard/{page}'

class LoginRequired(LoginRequiredMixin):
    login_url = '/login'
    redirect_field_name = 'redirect_to'

    def get_login_url(self) -> str:
        return reverse('back:login')

class IndexPageView(LoginRequired, TemplateView):
    ''' 
    Index Page 
    '''
    template_name = BASE_TEMPLATE.format(page='index')

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

    def get_queryset(self):
        return User.objects.all().order_by('first_name')

class UserPageView(LoginRequired, FormView):
    ''' 
    User Page 
    '''
    template_name = BASE_TEMPLATE.format(page='user')
    form_class = UserForm
    success_url = SUCCESS_URL.format(page='users/')

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

    def get_queryset(self):
        return Newsletter.objects.all().order_by('email')

class MessagePageView(LoginRequired, TemplateView):
    ''' 
    Message Page 
    Get messages from database
    '''
    template_name = BASE_TEMPLATE.format(page='message')

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

    def get_queryset(self):
        return Message.objects.all().order_by('-date_created')

class ProfilePageView(LoginRequired, FormView):
    ''' 
    Profile Page 
    '''
    template_name = BASE_TEMPLATE.format(page='profile')
    form_class = ProfilForm
    success_url = SUCCESS_URL.format(page='profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProfilForm(instance=User.objects.get(id=self.request.user.id))
        return context

    def post(self, request, *args, **kwargs):
        form = ProfilForm(request.POST, request.FILES, instance=User.objects.get(id=self.request.user.id))
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        
        context = self.form_invalid(form)
        return context

class LoginPageView(FormView):
    '''Sign in page'''
    template_name = BASE_TEMPLATE.format(page='login')
    form_class = LoginForm
    success_url = SUCCESS_URL

    def form_valid(self, form):
        user = User.objects.get(email=form.cleaned_data['email'])
        user = authenticate(username=user.username, password=form.cleaned_data['password'])
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

class LogoutPageView(TemplateView):
    '''Logout page'''
    template_name = BASE_TEMPLATE.format(page='logout')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)