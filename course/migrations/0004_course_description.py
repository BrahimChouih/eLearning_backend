# Generated by Django 3.0.6 on 2020-09-25 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20200925_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(max_length=2000, null=True),
        ),
    ]
