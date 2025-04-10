# Generated by Django 5.1.7 on 2025-03-22 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longUrl', models.URLField(verbose_name='Website URL')),
                ('shortUrl', models.URLField(max_length=20, verbose_name='Short URL')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Created Time')),
            ],
            options={
                'verbose_name': 'ShortUrl',
                'verbose_name_plural': 'ShortUrls',
            },
        ),
    ]
