# Generated by Django 5.2.3 on 2025-06-11 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0010_alter_image_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='nome',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
