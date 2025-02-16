# Generated by Django 4.2.17 on 2025-01-09 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coffee',
            options={'ordering': ['vendor', 'name']},
        ),
        migrations.AlterField(
            model_name='coffee',
            name='bean',
            field=models.CharField(choices=[('arabica', 'Arabica'), ('excelsa', 'Excelsa'), ('robusta', 'Robusta'), ('liberica', 'Liberica')]),
        ),
        migrations.AlterField(
            model_name='coffee',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='coffee',
            name='roast',
            field=models.CharField(choices=[('light', 'Light'), ('medium', 'Medium'), ('dark', 'Dark')]),
        ),
        migrations.AlterField(
            model_name='coffee',
            name='taste_profile',
            field=models.CharField(max_length=255),
        ),
    ]
