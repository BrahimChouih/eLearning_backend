# Generated by Django 3.0.6 on 2020-09-30 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0020_auto_20200930_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewer',
            name='rate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='course.Rater'),
        ),
    ]
