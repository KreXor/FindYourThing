from django.shortcuts import render
from django.utils import timezone
from .models import Activity
from django.http import HttpResponse

def activity_list(request):
    activities = Activity.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'activity/activity_list.html', {'activities': activities})
	
def activity_detail(request, activity_id):
    try:
        activity = Activity.objects.get(pk=activity_id)
    except Activity.DoesNotExist:
        raise Http404("Activity does not exist")
    return render(request, 'activity/activity_detail.html', {'activity': activity})