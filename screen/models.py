from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class text_post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Movie_Post(models.Model):
    video = models.FileField(null=False, blank=False, upload_to='video_cluster')
    video_title = models.CharField(max_length=100)

    def __str__(self):
        return self.video_title


class ImagePost(models.Model):
    image = models.ImageField(default='default.jpg', upload_to='image_cluster')
    image_title = models.CharField(max_length=100)

    def __str__(self):
        return self.image_title


