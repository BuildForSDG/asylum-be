# Generated by Django 2.2.10 on 2020-06-09 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_conditions'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='recommended',
            field=models.CharField(default='', max_length=50),
        ),
    ]
