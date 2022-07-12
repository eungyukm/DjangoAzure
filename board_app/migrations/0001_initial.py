# Generated by Django 4.0.6 on 2022-07-11 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoardInfoTable',
            fields=[
                ('board_info_idx', models.AutoField(primary_key=True, serialize=False)),
                ('board_info_name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ContentTable',
            fields=[
                ('content_idx', models.AutoField(primary_key=True, serialize=False)),
                ('content_subject', models.CharField(max_length=500)),
                ('content_text', models.TextField()),
                ('content_file', models.CharField(max_length=500, null=True)),
                ('content_date', models.DateTimeField()),
                ('content_board_idx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board_app.boardinfotable')),
                ('content_writer_idx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.usertable')),
            ],
        ),
    ]