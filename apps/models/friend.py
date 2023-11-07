from django.db import models
from apps.models.service import Service


class Friend(models.Model):
    objects = models.Manager()
    uid = models.CharField(blank=True, null=False, max_length=25, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, blank=True, null=True)
    service = models.ForeignKey(Service, related_name='service_friends', blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=['uid', ]),
        ]