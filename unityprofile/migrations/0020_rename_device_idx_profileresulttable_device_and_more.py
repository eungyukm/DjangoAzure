# Generated by Django 4.1.7 on 2023-03-13 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unityprofile', '0019_profileresulttable_project_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profileresulttable',
            old_name='device_idx',
            new_name='device',
        ),
        migrations.RenameField(
            model_name='profileresulttable',
            old_name='scenario_data_subject_idx',
            new_name='scenario_data',
        ),
    ]
