from django.contrib import admin
from .models import User, Request

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name', 'academic_email', 'academic_year')
    search_fields = ('user_name', 'academic_email')
    ordering = ('user_name',)

class RequestAdmin(admin.ModelAdmin):
    list_display = ('request_id', 'user_id', 'request_description', 'request_current_date', 'state')
    list_filter = ('state', 'request_current_date')
    search_fields = ('request_description',)

admin.site.register(User, UserAdmin)
admin.site.register(Request, RequestAdmin)


