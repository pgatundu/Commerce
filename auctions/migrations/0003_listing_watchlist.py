# Generated by Django 5.0.6 on 2024-06-04 10:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_category_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='watchlist',
            field=models.ManyToManyField(blank=True, null=True, related_name='listingWatchList', to=settings.AUTH_USER_MODEL),
        ),
    ]
