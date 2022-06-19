from django.views.generic import TemplateView, ListView, FormView
from django.contrib.auth import authenticate, login

from .forms import LoginForm
from .models import User
from front.models import Message, Newsletter

class IndexPageView(TemplateView):
    ''' 
    Index Page 
    '''
    template_name = 'pages/back/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

class UsersPageView(ListView):
    ''' 
    Users Page 
    '''
    template_name = 'pages/back/users.html'
    model = User
    paginate_by = 10
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.all().order_by('first_name')

class NewsletterPageView(ListView):
    ''' 
    Newsletter Page 
    Get all newsletter from database
    '''
    template_name = 'pages/back/newsletters.html'
    model = Newsletter
    paginate_by = 10
    context_object_name = 'newsletters'

    def get_queryset(self):
        return Newsletter.objects.all().order_by('email')

class MessagePageView(TemplateView):
    ''' 
    Message Page 
    Get messages from database
    '''
    template_name = 'pages/back/message.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = Message.objects.get(id=kwargs['id'])
        return context

class MessagesPageView(ListView):
    ''' List of all messages
    '''
    template_name = 'pages/back/messages.html'
    model = Message
    paginate_by = 10
    context_object_name = 'messages'

    def get_queryset(self):
        return Message.objects.all().order_by('-date_created')

class ProfilePageView(TemplateView):
    ''' 
    Profile Page 
    '''
    template_name = 'pages/back/profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['user'] = self.request.user
        return context

class LoginPageView(FormView):
    '''Sign in page'''
    template_name = 'pages/back/login.html'
    form_class = LoginForm
    success_url = '/dashboard/'

    def form_valid(self, form):
        user = User.objects.get(email=form.cleaned_data['email'])
        user = authenticate(username=user.username, password=form.cleaned_data['password'])
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            return self.form_invalid(form)
    