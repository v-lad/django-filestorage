from django.contrib import admin
from .models import UploadedFileModel
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class UploadedFileModelInline(admin.TabularInline):
    model = UploadedFileModel
    extra = 0

    readonly_fields = ['slug', 'upload_time', 'deadline', 'size', 'file']


@admin.register(UploadedFileModel)
class UploadedFileModelAdmin(admin.ModelAdmin):
    readonly_fields = ('upload_time', 'user')
    fieldsets = (
        ('', {
            'classes': ('extrapretty'),
            'fields': ('file', 'user')
        }),
        ('Date', {
            'fields': ('upload_time', 'deadline')
        }),
    )

class CustomUserAdmin(UserAdmin):
    def __init__(self, *args, **kwargs):
        super(UserAdmin,self).__init__(*args, **kwargs)
        UserAdmin.list_display = list(UserAdmin.list_display)

        UserAdmin.inlines = list(UserAdmin.inlines) + [UploadedFileModelInline]


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
