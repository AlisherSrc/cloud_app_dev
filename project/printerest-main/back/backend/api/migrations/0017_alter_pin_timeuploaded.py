# Generated by Django 3.2 on 2024-10-17 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_alter_userprofile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='timeUploaded',
            field=models.DateTimeField(null=True),
        ),
    ]