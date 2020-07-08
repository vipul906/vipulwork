from django.contrib import admin

# Register your models here.
from .models import User, ActivityPeriod


class ChoiceInline(admin.TabularInline):
    model = ActivityPeriod
    extra = 0


class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['user_name']}),
        ('User information', {'fields': ['user_id', 'tz'],
                              'classes': ['collapse']})
    ]
    inlines = [ChoiceInline]


admin.site.register(User, UserAdmin)
