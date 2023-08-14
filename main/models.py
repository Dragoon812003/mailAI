from django.db import models
from django.utils import timezone
from PIL import Image
from . import utils

# Create your models here.

class Developer(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=64)
    github_link = models.CharField(max_length=64)
    linkedin_link = models.CharField(max_length=64)
    profile_pic = models.ImageField(upload_to=utils.developer_profile_pic_path)
    timestamp = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self): return self.name

    def save(self, *args, **kwargs):
        if not self.timestamp:
            timestamp = timezone.now().strftime('%Y%m%d_%H%M%S')
            self.timestamp = timestamp
        super().save(*args, **kwargs)
