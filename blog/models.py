from django.db import models
from django.urls import reverse
from django.utils import timezone
from PIL import Image
from django.core.validators import FileExtensionValidator
from django.template.defaultfilters import slugify



class Album(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(null=True,blank=True)
    poster = models.ImageField(upload_to='posters')
    date_posted = models.DateTimeField(default=timezone.now)
    views = models.IntegerField(default=0)
    # track  = models.ManyToManyField(Track,related_name='tracks')


    def __str__(self):
        return f"{self.title}"

       
    def get_absolute_url(self):
        return reverse("album_track_detail",args={self.slug})

    def get_absolute_url_afteremail(self):
        return reverse("album_afteremail_detail",args={self.slug })

    def get_absolute_download_tracks_url(self):
        return reverse("can_download_tracks_detail",args={self.slug })

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.poster.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail = (output_size)
            img.save(self.poster.path)



class Track(models.Model):
    track_title = models.CharField(max_length=60)
    track = models.FileField(upload_to='tracks',)
    album = models.ManyToManyField(Album,related_name='album')
    track_duration = models.CharField(max_length=10,default="3:15")
    # album_id = models.CharField(max_length=100,default=1)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.track_title}"

    def track_count(self):
        return self.album.track.count

    def get_download_now_url(self):
        return reverse("download_now",args={self.album.title})


class Vtrack(models.Model):
    user_code = models.IntegerField(default=0)
    user_platform = models.CharField(max_length=100)
    vcount = models.IntegerField(default=0)

    def __str__(self):
        return f"User's platform is {self.user_platform}"



class TrackByEmail(models.Model):
    email = models.EmailField()
    album_title = models.CharField(max_length=100)
    random_id = models.IntegerField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"email is {self.email}"

class VerifyEmail(models.Model):
    youremail = models.EmailField()

    def __str__(self):
        return f"{self.youremail }"
    


class Gallery(models.Model):
    caption = models.CharField(max_length=30)
    image = models.ImageField(upload_to='gallery',validators=[FileExtensionValidator(allowed_extensions=['jpg'])])
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.caption}"

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    poster = models.ImageField(upload_to='event_posters')
    start_date = models.DateTimeField(default=timezone.now)
    started = models.BooleanField(default=False)
    date_posted = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"{self.title }"