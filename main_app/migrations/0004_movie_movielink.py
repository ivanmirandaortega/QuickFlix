# Generated by Django 4.0.4 on 2022-04-29 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_movie_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movielink',
            field=models.CharField(default=' ', max_length=250),
            preserve_default=False,
        ),
    ]
