# Generated by Django 2.2.6 on 2020-05-29 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0008_profile_full_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='user_name',
        ),
        migrations.AlterField(
            model_name='profile',
            name='job_location',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='job_title',
            field=models.TextField(blank=True, max_length=50),
        ),
    ]
