# Generated by Django 3.0.6 on 2020-09-27 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_auto_20200927_2028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='cover',
        ),
    ]
