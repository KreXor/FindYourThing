from django.shortcuts import render
from django.utils import timezone
from .models import Activity

def activity_list(request):
    activities = Activity.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'activity/activity_list.html', {'activities': activities})
