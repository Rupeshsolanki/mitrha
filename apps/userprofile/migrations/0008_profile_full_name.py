# Generated by Django 2.2.6 on 2020-05-29 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0007_auto_20200529_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='full_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
