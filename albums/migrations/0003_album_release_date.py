# Generated by Django 4.0.4 on 2022-05-09 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_album_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
