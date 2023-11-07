from django.db import models
from apps.models.relation import Relation


class Conversation(models.Model):
    class ConversationTypes(models.IntegerChoices):
        USER = (1, "USER")
        GROUP = (2, "GROUP")
        PAGE = (3, "PAGE")

    objects = models.Manager()
    uid = models.CharField(blank=True, null=False, max_length=25, unique=True)
    type = models.IntegerField(choices=ConversationTypes.choices, default=ConversationTypes.USER, max_length=10)

    def __str__(self):
        return self.uid

    class Meta:
        indexes = [
            models.Index(fields=['uid', ]),
        ]


class Message(models.Model):
    objects = models.Manager()
    uid = models.CharField(max_length=100)
    relation = models.ForeignKey(Relation, related_name='relation_messages', blank=False, null=False,
                                 on_delete=models.CASCADE, to_field='uid')
    conversation = models.ForeignKey(Conversation, related_name='conversation_messages', blank=False, null=False,
                                     on_delete=models.CASCADE, to_field='uid')
    content = models.TextField(blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['uid', ]),
        ]

