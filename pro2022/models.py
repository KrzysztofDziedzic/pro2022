from django.conf import settings
from django.db import models
from django.utils import timezone


class Page(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    description = models.CharField(max_length=1000)
    keywords = models.CharField(max_length=500)
    scripts = models.TextField()
    tracking = models.CharField(max_length=500)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title