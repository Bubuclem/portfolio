'''
Admin site for the back app
'''
from django.contrib import admin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from back.models import User
from django.contrib.auth.admin import UserAdmin

class UserTool(UserAdmin):
    '''
    User admin tool
    '''
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)
    filter_horizontal = ()
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email','picture_profile')}),
        ('Permissions', {'fields': ('is_active', 'is_staff',
        'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )

    form = UserChangeForm
    add_form = UserCreationForm

    def get_queryset(self, request):
        queryset = super(UserTool, self).get_queryset(request)
        queryset = queryset.order_by('username')
        return queryset

admin.site.register(User, UserTool)
