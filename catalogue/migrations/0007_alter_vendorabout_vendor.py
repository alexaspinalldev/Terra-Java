# Generated by Django 4.2.17 on 2025-01-16 23:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalogue', '0006_alter_vendorabout_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendorabout',
            name='vendor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='vendorabout', to=settings.AUTH_USER_MODEL),
        ),
    ]