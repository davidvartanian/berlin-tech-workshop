# Generated by Django 2.1.7 on 2019-03-29 15:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='links', to=settings.AUTH_USER_MODEL),
        ),
    ]
