# Generated by Django 4.1.1 on 2023-05-19 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='thumbnaill',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
