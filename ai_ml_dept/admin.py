from django.contrib import admin
from django.contrib.admin.models import LogEntry

admin.site.site_header = "AI & ML Department Admin"
admin.site.site_title = "AI & ML Department Admin Portal"
admin.site.index_title = "Welcome to AI & ML Department Admin Portal"

# Unregister default LogEntry if not needed
admin.site.unregister(LogEntry)

# Custom admin CSS
class CustomAdminSite(admin.AdminSite):
    def each_context(self, request):
        context = super().each_context(request)
        context['site_header'] = self.site_header
        context['site_title'] = self.site_title
        context['index_title'] = self.index_title
        return context

# Apply custom CSS
from django.contrib.admin import AdminSite
AdminSite.enable_nav_sidebar = False