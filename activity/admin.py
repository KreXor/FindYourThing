from django.contrib import admin

from .models import Activity
from .models import ActivityType
from .models import ActivityAddress

admin.site.register(Activity)
admin.site.register(ActivityType)
admin.site.register(ActivityAddress)

class AddressLine(admin.StackedInline):
    model = ActivityAddress

class ActivityAdmin(admin.ModelAdmin):
    model = Activity
    inlines = [ AddressLine ]