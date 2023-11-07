from django.db import models
from apps.models.friend import Friend
from apps.models.user import User


class Relation(models.Model):
    objects = models.Manager()
    uid = models.CharField(blank=True, null=False, max_length=25, unique=True)
    friend = models.ForeignKey(Friend, related_name='friend_relations', blank=False, null=False,
                               on_delete=models.CASCADE, to_field='uid')
    user = models.ForeignKey(User, related_name='user_relations', blank=True, null=True,
                             on_delete=models.CASCADE, to_field='uid')

    def __str__(self):
        return self.uid

    class Meta:
        indexes = [
            models.Index(fields=['uid', ]),
        ]
