# Generated by Django 3.0.6 on 2020-09-27 13:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0005_auto_20200926_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(null=True, related_name='Course_students', to=settings.AUTH_USER_MODEL),
        ),
    ]
