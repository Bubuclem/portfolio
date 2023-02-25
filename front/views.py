'''
Views for front app
'''
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView

from front.models import SocialMedia, Tool, Address, ContactMe, AboutMe, Newsletter, Message
from front.forms import contactForm, newsletterForm


class BaseView(TemplateView):
    ''' 
    Generic TemplateView
    Return context with social
    '''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['social_media'] = SocialMedia.objects.all()
        return context


class IndexPageView(BaseView):
    ''' 
    Index Page
    Get foor first tools from database filtred by 'order'
    '''
    template_name = 'pages/front/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tools'] = Tool.objects.order_by('order')[:4]
        context['about_me'] = AboutMe.objects.first()
        context['newsletter'] = newsletterForm()
        return context

    ''' 
    Post the newsletter
    Check if the email exist in database
    '''

    def post(self, request, *args, **kwargs):
        form = newsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if Newsletter.objects.filter(email=email).exists() is False:
                form.save()
        return redirect('/')


class ToolsPageView(BaseView):
    ''' 
    Tools Page
    Get all tools from database
    '''
    template_name = 'pages/front/tools.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tools'] = Tool.objects.all()
        return context


class AboutPageView(BaseView):
    ''' 
    About Page
    '''
    template_name = 'pages/front/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newsletter'] = newsletterForm()
        return context


class ContactPageView(BaseView):
    ''' 
    Contact Page
    Get all addresses from database
    '''
    template_name = 'pages/front/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['addresses'] = Address.objects.all()
        context['form'] = contactForm()
        context['contacts'] = ContactMe.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        '''
        Post the contact form
        Check how many messsages about this email have been sent
        if he has sent 5 messages, return error message
        '''
        form = contactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if Message.objects.filter(email=email).count() >= 5:
                form.add_error(
                    'email', 'You have sent 5 messages about this email. Please try again later.')
            else:
                form.save()
        return redirect('/contact/')

def page_not_found(request, exception):
    ''' 
    View 404 
    Return 404 page if page not found
    '''
    return render(request, 'pages/front/404.html', status=404)

def server_error(request):
    ''' 
    View 500 
    Return 500 page if server error
    '''
    return render(request, 'errors/500.html', status=500)
