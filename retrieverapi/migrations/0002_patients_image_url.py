# Generated by Django 4.1.3 on 2022-12-05 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retrieverapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patients',
            name='image_url',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]