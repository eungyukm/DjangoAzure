# Generated by Django 4.1.7 on 2023-03-13 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unityprofile', '0020_rename_device_idx_profileresulttable_device_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profileresulttable',
            old_name='profile_result_idx',
            new_name='profile_result_id',
        ),
    ]
