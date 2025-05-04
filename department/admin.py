from django.contrib import admin
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from .models import *

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_published')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'content')
    actions = ['publish_news']

    def publish_news(self, request, queryset):
        updated = queryset.update(is_published=True)
        self.message_user(request, f"{updated} news items published successfully.")
        
        # Send email to subscribers
        if updated > 0:
            email_config = EmailConfig.objects.first()
            if email_config:
                subscribers = EmailSubscriber.objects.filter(is_active=True)
                subject = "New Updates from AI & ML Department"
                
                for news in queryset.filter(is_published=True):
                    message = f"""
                    <h2>{news.title}</h2>
                    <p>{news.content[:200]}...</p>
                    <p>Read more on our website!</p>
                    """
                    
                    email = EmailMessage(
                        subject,
                        message,
                        email_config.default_from_email,
                        [sub.email for sub in subscribers],
                    )
                    email.content_subtype = "html"
                    
                    # Configure email settings
                    settings.EMAIL_HOST = email_config.email_host
                    settings.EMAIL_PORT = email_config.email_port
                    settings.EMAIL_HOST_USER = email_config.email_username
                    settings.EMAIL_HOST_PASSWORD = email_config.email_password
                    settings.EMAIL_USE_TLS = email_config.email_use_tls
                    settings.EMAIL_USE_SSL = email_config.email_use_ssl
                    
                    try:
                        email.send()
                    except Exception as e:
                        self.message_user(request, f"Error sending emails: {str(e)}", level=messages.ERROR)
    publish_news.short_description = "Publish selected news and notify subscribers"

class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'email')
    search_fields = ('name', 'designation', 'qualification')
    list_filter = ('designation',)

class TimetableAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')

class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date', 'upload_date')
    list_filter = ('event_date',)
    search_fields = ('title', 'description')

class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'submission_date', 'is_responded')
    list_filter = ('is_responded', 'submission_date')
    search_fields = ('name', 'email', 'subject')
    readonly_fields = ('submission_date',)

class EmailSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('email',)

class EmailConfigAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Only allow one configuration
        return not EmailConfig.objects.exists()

admin.site.register(News, NewsAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Timetable, TimetableAdmin)
admin.site.register(GalleryImage, GalleryImageAdmin)
admin.site.register(ContactSubmission, ContactSubmissionAdmin)
admin.site.register(EmailSubscriber, EmailSubscriberAdmin)
admin.site.register(EmailConfig, EmailConfigAdmin)