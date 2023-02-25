'''
Views for profil app
'''
from django.views.generic import TemplateView

from profil.models import Work, Education, Project, CategorieUse, Use, About

class ProfilView(TemplateView):
    '''
    Class of profil view
    '''
    template_name = 'pages/page.html'

    def get_context_data(self, **kwargs):
        context = super(ProfilView, self).get_context_data(**kwargs)
        context['works'] = Work.objects.all().order_by('-order')
        context['educations'] = Education.objects.all().order_by('-order')
        context['projects'] = Project.objects.all()
        context['categories'] = CategorieUse.objects.all()
        context['uses'] = Use.objects.all()
        context['abouts'] = About.objects.all()
        return context