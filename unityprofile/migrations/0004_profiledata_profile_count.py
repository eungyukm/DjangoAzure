# Generated by Django 4.1.7 on 2023-03-06 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unityprofile', '0003_profiledata_project_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiledata',
            name='profile_count',
            field=models.IntegerField(default='-1'),
        ),
    ]
