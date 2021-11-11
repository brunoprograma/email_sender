from django.contrib import admin

from .models import EmailMessage


@admin.register(EmailMessage)
class EmailMessageAdmin(admin.ModelAdmin):
    list_display = ['subject', 'created_at', 'status']
    list_filter = ['status']
    date_hierarchy = 'created_at'
    search_fields = ['recipients__email']
