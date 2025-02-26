# Generated by Django 3.2 on 2024-03-31 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0003_channel_channel_art'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='Facebook',
            field=models.URLField(default='https://facebook.com/'),
        ),
        migrations.AddField(
            model_name='channel',
            name='X',
            field=models.URLField(default='https://x.com/'),
        ),
        migrations.AddField(
            model_name='channel',
            name='buisness_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='channel',
            name='buisness_location',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='channel',
            name='instagram',
            field=models.URLField(default='https://instagram.com/'),
        ),
        migrations.AddField(
            model_name='channel',
            name='make_buisness_email_public',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='channel',
            name='make_buisness_loaction_public',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='channel',
            name='total_views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='channel',
            name='website',
            field=models.URLField(default='https://my-website.html/'),
        ),
    ]
