from django.contrib import admin
from .models import EmailMessage  # , Recipient
from .forms import EmailMessageForm


# @admin.register(Recipient)
# class RecipientAdmin(admin.ModelAdmin):
#     list_display = ['email']
#     search_fields = ['email']


@admin.register(EmailMessage)
class EmailMessageAdmin(admin.ModelAdmin):
    def re_send_messages(self, request, queryset):
        rows_updated = 0
        for message in queryset.exclude(status='p'):
            message.status = 'p'
            message.save()  # needs to call save method
            rows_updated += 1

        if rows_updated == 1:
            message = 'Your message will be re-sended'
        else:
            message = 'Your messages will be re-sended'
        self.message_user(request, message)
    re_send_messages.short_description = 'Re-send messages'

    form = EmailMessageForm
    list_display = ['subject', 'created_at', 'status']
    list_filter = ['status']
    date_hierarchy = 'created_at'
    search_fields = ['recipients__email']
    actions = ['re_send_messages']
