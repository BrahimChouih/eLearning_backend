# Generated by Django 3.0.6 on 2020-09-30 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0018_auto_20200930_1326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewer',
            name='rate',
        ),
    ]