# Generated by Django 4.0.5 on 2022-07-08 18:00

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0003_alter_user_picture_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture_profile',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='PNG', keep_meta=True, null=True, quality=-1, scale=None, size=[250, 250], upload_to='users/pictures/'),
        ),
    ]
