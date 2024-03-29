# Generated by Django 3.2.7 on 2021-09-18 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='spotifytoken',
            name='access_token',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='spotifytoken',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='spotifytoken',
            name='expires_in',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='spotifytoken',
            name='refresh_token',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='spotifytoken',
            name='token_type',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='spotifytoken',
            name='user',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]
