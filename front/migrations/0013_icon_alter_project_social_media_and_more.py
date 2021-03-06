# Generated by Django 4.0.5 on 2022-07-09 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0012_message_date_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('path', models.TextField()),
                ('view_box', models.CharField(blank=True, default='0 0 24 24', max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='social_media',
            field=models.ManyToManyField(to='front.icon'),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='icon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.icon'),
        ),
    ]
