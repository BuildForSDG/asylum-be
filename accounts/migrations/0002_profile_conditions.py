# Generated by Django 2.2.10 on 2020-06-08 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disorders', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='conditions',
            field=models.ManyToManyField(to='disorders.Disorder'),
        ),
    ]
