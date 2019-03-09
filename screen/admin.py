from django.contrib import admin
from .models import text_post
from .models import Movie_Post
from .models import ImagePost


# Register your models here.
admin.site.register(text_post)
admin.site.register(Movie_Post)
admin.site.register(ImagePost)
