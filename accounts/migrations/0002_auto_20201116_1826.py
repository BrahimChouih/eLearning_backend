# Generated by Django 3.0.6 on 2020-11-16 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='course_made_by_me',
            field=models.ManyToManyField(blank=True, related_name='course_made_by_me', to='course.Course'),
        ),
        migrations.AddField(
            model_name='account',
            name='purchased_courses',
            field=models.ManyToManyField(blank=True, related_name='purchased_courses', to='course.Course'),
        ),
    ]
