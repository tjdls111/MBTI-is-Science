# Generated by Django 3.2.6 on 2021-11-20 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_tmdb_pk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(default='0000-00-00'),
        ),
    ]
