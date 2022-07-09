from django.db import models
from django.utils.html import mark_safe

MARK_SAFE_SVG = '<svg style="color:white;" width="25px" height="25px" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="{view_box}" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="{path}" /></svg>'

class Icon(models.Model):
    '''
    Icon model, used to store the icons used in the application.
    '''
    name = models.CharField(max_length=100)
    path = models.TextField()
    view_box = models.CharField(max_length=20, default='0 0 24 24', blank=True)
    
    def __str__(self):
        return self.name

    def to_svg(self):
        '''
        Method used to display the icon in the admin panel.
        '''
        return mark_safe(MARK_SAFE_SVG.format(view_box=self.view_box, path=self.path))

class SocialMedia(models.Model):
    ''' 
    Class of social media 
    '''
    name = models.CharField(max_length=255)
    url = models.URLField()
    icon = models.ForeignKey(Icon, on_delete=models.CASCADE)
    order = models.IntegerField()
    class Meta:
        ordering = ['order']
    def __str__(self):
        return self.name

class Tool(models.Model):
    ''' 
    Class of developpement tools 
    '''
    name = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    icon = models.URLField()
    order = models.IntegerField()
    class Meta:
        ordering = ['order']
    def __str__(self):
        return self.name

class Address(models.Model):
    ''' 
    Class of address 
    Address where you can find me
    '''
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
        ordering = ['country']
    def __str__(self):
        return self.street + ' ' + self.city + ' ' + self.zip + ' ' + self.country

class Project(models.Model):
    ''' 
    Class of project 
    Not used yet
    '''
    name = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    image = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    tools = models.ManyToManyField(Tool)
    social_media = models.ManyToManyField(Icon)
    class Meta:
        verbose_name_plural = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['name']
    def __str__(self):
        return self.name

class ContactMe(models.Model):
    ''' 
    Class for contact me 
    Email show on contact page
    '''
    email = models.EmailField()
    class Meta:
        verbose_name = 'Contact me'
        verbose_name_plural = 'Contact me'
        ordering = ['email']
    def __str__(self):
        return self.email

class AboutMe(models.Model):
    ''' 
    Class about me 
    Info about me in the main page
    '''
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    class Meta:
        verbose_name = 'About me'
        verbose_name_plural = 'About me'
        ordering = ['name']
    def __str__(self):
        return self.name

class Stats(models.Model):
    ''' 
    class of stats about me 
    Not used yet
    '''
    name = models.CharField(max_length=255)
    value = models.IntegerField()
    class Meta:
        verbose_name = 'Stat'
        verbose_name_plural = 'Stats'
        ordering = ['name']
    def __str__(self):
        return self.name

class Newsletter(models.Model):
    ''' 
    Class for newsletter 
    user subscribe to newsletter
    '''
    email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'
        ordering = ['email']
    def __str__(self):
        return self.email

class Message(models.Model):
    '''' 
    Class for contact me
    user send a message to me
    '''
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        ordering = ['last_name']
    def __str__(self):
        return self.email