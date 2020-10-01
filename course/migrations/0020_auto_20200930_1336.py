# Generated by Django 3.0.6 on 2020-09-30 12:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0019_remove_reviewer_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='Course_students', to=settings.AUTH_USER_MODEL),
        ),
    ]
