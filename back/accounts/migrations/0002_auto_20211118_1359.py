# Generated by Django 3.2.6 on 2021-11-18 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='mbti',
            field=models.CharField(choices=[('ENTJ', 'ENTJ'), ('ENTP', 'ENTP'), ('ENFJ', 'ENFJ'), ('ENFP', 'ENFP'), ('ESTJ', 'ESTJ'), ('ESTP', 'ESTP'), ('ESFJ', 'ESFJ'), ('ESFP', 'ESFP'), ('INTJ', 'INTJ'), ('INTP', 'INTP'), ('INFJ', 'INFJ'), ('INFP', 'INFP'), ('ISTJ', 'ISTJ'), ('ISTP', 'ISTP'), ('ISFJ', 'ISFJ'), ('ISFP', 'ISFP')], default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]