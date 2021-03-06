# Generated by Django 3.0.3 on 2020-02-19 15:31

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('poster', models.ImageField(upload_to='posters')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('views', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='gallery')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='TrackByEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('album_title', models.CharField(max_length=100)),
                ('random_id', models.IntegerField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='VerifyEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('youremail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Vtrack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_code', models.IntegerField(default=0)),
                ('user_platform', models.CharField(max_length=100)),
                ('vcount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_title', models.CharField(max_length=60)),
                ('track', models.FileField(upload_to='tracks', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])),
                ('track_duration', models.CharField(default='3:15', max_length=10)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('album', models.ManyToManyField(related_name='album', to='blog.Album')),
            ],
        ),
    ]
