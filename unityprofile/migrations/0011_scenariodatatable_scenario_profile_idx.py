# Generated by Django 4.1.7 on 2023-03-09 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unityprofile', '0010_scenariodatatable'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenariodatatable',
            name='scenario_profile_idx',
            field=models.IntegerField(default=0),
        ),
    ]
