# Generated by Django 4.0.5 on 2022-07-03 09:17

import Blogger.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.IntegerField(default=1, unique=True)),
                ('post_name', models.CharField(max_length=100)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('Topic', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('rank', models.FloatField()),
                ('post_image', models.ImageField(blank=True, null=True, upload_to=Blogger.models.Post.uploadPhoto)),
                ('post_files', models.ImageField(blank=True, null=True, upload_to=Blogger.models.Post.uploadFile)),
            ],
        ),
    ]
