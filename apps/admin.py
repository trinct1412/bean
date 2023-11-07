from django.contrib import admin
from apps.models import Conversation, Message, Friend, Relation, Service, User


class CustomModelAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        fields_ = [field.name for field in model._meta.fields if field.name not in ('uid', "id")]
        self.list_display = fields_
        self.search_fields = fields_
        super(CustomModelAdmin, self).__init__(model, admin_site)


class ConversationAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        fields_ = [field.name for field in model._meta.fields]
        self.list_display = fields_
        self.search_fields = fields_
        super(ConversationAdmin, self).__init__(model, admin_site)


admin.site.register(Conversation, ConversationAdmin)
admin.site.register(Message, CustomModelAdmin)
admin.site.register(Friend, CustomModelAdmin)
admin.site.register(Relation, CustomModelAdmin)
admin.site.register(Service, CustomModelAdmin)
admin.site.register(User, CustomModelAdmin)
