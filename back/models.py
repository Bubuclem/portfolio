'''
Back models
'''
from django_resized import ResizedImageField
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    '''
    User model
    '''
    picture_profile = ResizedImageField(size=[250, 250], crop=['middle', 'center'],
    force_format='PNG', upload_to='users/pictures/', blank=True, null=True)

    class Meta:
        '''
        Meta class for User model
        '''
        verbose_name = 'Utilisateur'
        verbose_name_plural = 'Utilisateurs'

    def __str__(self):
        return self.username

    def get_picture_profile(self):
        '''
        Get picture profile
        '''
        if self.picture_profile:
            return self.picture_profile.url
        else:
            return None

    def _create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')

        username = self.normalize_username(username)

        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, username, email, password=None, **extra_fields):
        '''
        Create user
        '''
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        '''
        Create superuser
        '''
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)
