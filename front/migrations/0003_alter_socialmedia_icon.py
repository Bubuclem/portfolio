# Generated by Django 4.0.5 on 2022-06-03 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0002_address_tool_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedia',
            name='icon',
            field=models.TextField(),
        ),
    ]
