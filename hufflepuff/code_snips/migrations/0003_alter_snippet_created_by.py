# Generated by Django 3.2.9 on 2021-11-16 02:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('code_snips', '0002_auto_20211113_0244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
