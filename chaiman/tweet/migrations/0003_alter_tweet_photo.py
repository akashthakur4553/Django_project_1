# Generated by Django 5.1.6 on 2025-02-22 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0002_alter_tweet_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='tweet_images/'),
        ),
    ]
