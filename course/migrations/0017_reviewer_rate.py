# Generated by Django 3.0.6 on 2020-09-30 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0016_auto_20200928_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewer',
            name='rate',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='course.Rater'),
            preserve_default=False,
        ),
    ]