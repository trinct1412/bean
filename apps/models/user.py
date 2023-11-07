from django.db import models
from apps.models.service import Service
from django.utils.translation import gettext_lazy as _


class User(models.Model):
    class UserType(models.TextChoices):
        USER = 'User', _('User')
        PAGE = 'Page', _('Page')

    objects = models.Manager()
    uid = models.CharField(blank=True, null=False, max_length=25, unique=True)
    name = models.CharField(max_length=255)
    short_token = models.TextField()
    token = models.TextField()
    expires_in = models.DateTimeField(blank=True, null=True)
    is_valid = models.BooleanField(default=False)
    service = models.ForeignKey(Service, related_name='service_users', blank=False, null=False,
                                on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=UserType.choices, default=UserType.USER)

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=['uid', ]),
        ]
