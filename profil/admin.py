'''
Admin panel for profil app
'''
from django.contrib import admin

from profil.models import Work, Education, Project, CategorieUse, Use, About

class WorkAdmin(admin.ModelAdmin):
    '''
    Class of work admin
    '''
    list_display = ('name', 'post', 'period_start', 'period_end', 'current', 'order')
    list_filter = ('name', 'post', 'period_start', 'period_end', 'current', 'order')
    search_fields = ('name', 'post', 'period_start', 'period_end', 'current', 'order')
    ordering = ('order',)

class EducationAdmin(admin.ModelAdmin):
    '''
    Class of education admin
    '''
    list_display = ('name', 'degree', 'period_start', 'period_end', 'current', 'order')
    list_filter = ('name', 'degree', 'period_start', 'period_end', 'current', 'order')
    search_fields = ('name', 'degree', 'period_start', 'period_end', 'current', 'order')
    ordering = ('order',)

class ProjectAdmin(admin.ModelAdmin):
    '''
    Class of project admin
    '''
    list_display = ('name', 'description', 'url', 'order')
    list_filter = ('name', 'description', 'url', 'order')
    search_fields = ('name', 'description', 'url', 'order')
    ordering = ('order',)

class CategorieUseAdmin(admin.ModelAdmin):
    '''
    Class of categorie use admin
    '''
    list_display = ('name', 'order')
    list_filter = ('name', 'order')
    search_fields = ('name', 'order')
    ordering = ('order',)

class UseAdmin(admin.ModelAdmin):
    '''
    Class of use admin
    '''
    list_display = ('name', 'categorie', 'order')
    list_filter = ('name', 'categorie', 'order')
    search_fields = ('name', 'categorie', 'order')
    ordering = ('order',)

class AboutAdmin(admin.ModelAdmin):
    '''
    Class of about admin
    '''
    list_display = ('description',)

admin.site.register(Work, WorkAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(CategorieUse, CategorieUseAdmin)
admin.site.register(Use, UseAdmin)
admin.site.register(About, AboutAdmin)
