# Generated by Django 3.2.6 on 2021-11-20 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='tmdb_pk',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
