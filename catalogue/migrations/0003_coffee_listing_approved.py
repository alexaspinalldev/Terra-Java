# Generated by Django 4.2.17 on 2025-01-10 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_alter_coffee_options_alter_coffee_bean_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffee',
            name='listing_approved',
            field=models.BooleanField(default=False),
        ),
    ]
