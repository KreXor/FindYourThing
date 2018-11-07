from django.contrib import admin

from .models import Activity
from .models import ActivityType

admin.site.register(Activity)
admin.site.register(ActivityType)
