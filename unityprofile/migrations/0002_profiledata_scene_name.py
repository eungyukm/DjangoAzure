# Generated by Django 4.1.7 on 2023-03-06 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unityprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiledata',
            name='scene_name',
            field=models.CharField(default='none', max_length=100),
        ),
    ]
