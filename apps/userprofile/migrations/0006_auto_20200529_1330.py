# Generated by Django 2.2.6 on 2020-05-29 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_auto_20200529_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='job_loc',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='profile',
            name='job_title',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
