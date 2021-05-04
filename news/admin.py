from django.contrib import admin

from news import models

admin.site.register(models.News)
admin.site.register(models.Slider)
