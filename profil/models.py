'''
Models of the profil application
'''
from django.db import models

class Work(models.Model):
    ''' 
    Class of work 
    '''
    name = models.CharField(max_length=255)
    post = models.CharField(max_length=255)
    period_start = models.DateField()
    period_end = models.DateField()
    current = models.BooleanField(default=False)
    order = models.IntegerField()
    class Meta:
        '''
        Meta class for Work
        '''
        verbose_name = 'Work'
        verbose_name_plural = 'Works'
        ordering = ['order']

    def __str__(self):
        return str(self.name)

class Education(models.Model):
    ''' 
    Class of education 
    '''
    name = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    period_start = models.DateField()
    period_end = models.DateField()
    current = models.BooleanField(default=False)
    order = models.IntegerField()
    class Meta:
        '''
        Meta class for Education
        '''
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'
        ordering = ['order']

    def __str__(self):
        return str(self.name)

class Project(models.Model):
    ''' 
    Class of project 
    '''
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    order = models.IntegerField()
    class Meta:
        '''
        Meta class for Project
        '''
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['order']

    def __str__(self):
        return str(self.name)

class CategorieUse(models.Model):
    ''' 
    Class of categorie use 
    '''
    name = models.CharField(max_length=255)
    order = models.IntegerField()
    class Meta:
        '''
        Meta class for CategorieUse
        '''
        verbose_name = 'Use categorie'
        verbose_name_plural = 'Uses categories'
        ordering = ['order']

    def __str__(self):
        return str(self.name)

class Use(models.Model):
    '''
    Class of use
    '''
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    categorie = models.ForeignKey(CategorieUse, on_delete=models.CASCADE)
    order = models.IntegerField()

    class Meta:
        '''
        Meta class for Use
        '''
        verbose_name = 'Use'
        verbose_name_plural = 'Uses'
        ordering = ['order']

    def __str__(self):
        return str(self.name)
