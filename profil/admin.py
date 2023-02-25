'''
Admin panel for profil app
'''
from django.contrib import admin

from profil.models import Work, Education, Project

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

admin.site.register(Work, WorkAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Project, ProjectAdmin)
