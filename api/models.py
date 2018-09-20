from django.db import models

# Create your models here.

class Music(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    dateCreate = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255)
    src = models.FileField(upload_to="static_files/music/", null=False, blank=True)
    pic = models.ImageField(upload_to="static_files/cover/", null=True, blank=True, default="none_pic")
    likes = models.IntegerField(default="0")
    duration = models.IntegerField(default="0", null=False)

class Meta:
    ordering = ('created',)
