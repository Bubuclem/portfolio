from django.contrib import admin

from .models import SocialMedia, Tool, Address, Project, ContactMe, AboutMe, Stats, Newsletter, Message

admin.site.register(SocialMedia)

class ToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)

admin.site.register(Tool,ToolAdmin)

class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'city', 'zip', 'country')

admin.site.register(Address,AddressAdmin)
admin.site.register(Project)
admin.site.register(ContactMe)
admin.site.register(AboutMe)
admin.site.register(Stats)
admin.site.register(Newsletter)

class MessageAdmin(admin.ModelAdmin):
    list_display = ('email', 'subject', 'date_created')

admin.site.register(Message,MessageAdmin)