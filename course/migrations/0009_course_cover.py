# Generated by Django 3.0.6 on 2020-09-27 19:29

import course.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_remove_course_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='cover',
            field=models.ImageField(default='', upload_to=course.models.uploadImage),
            preserve_default=False,
        ),
    ]