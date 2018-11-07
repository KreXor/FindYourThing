from django.conf import settings
from django.db import models
from django.utils import timezone

class ActivityType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Activity(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    type = models.ForeignKey(ActivityType, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    webpage = models.URLField(max_length=200)
    instagram = models.URLField(max_length=200)
    facebook = models.URLField(max_length=200)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
