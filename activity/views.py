import json

from django.shortcuts import render
from django.utils import timezone
from .models import Activity
from django.http import HttpResponse
from django.core import serializers

from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def activity_list(request):
    if request.is_ajax():
        location = request.POST.get('location')
        if(location == ''):
            return HttpResponse(json.dumps(''),
			    content_type='application/json')
        location = location.split(',')
        activities = Activity.objects.filter(address__contains=location[0]).order_by('published_date')
        # do whatever processing you need
        # user.some_property = whatever

        # send back whatever properties you have updated
        #json_response = {'activities': activities}
        json_response = serializers.serialize("json", activities.all())
        #json_response = {'location': location}
        return HttpResponse(json.dumps(json_response),
            content_type='application/json')
	
    activities = Activity.objects.order_by('published_date')
    return render(request, 'activity/activity_list.html', {'activities': activities})
	
def activity_detail(request, activity_id):
    try:
        activity = Activity.objects.get(pk=activity_id)
    except Activity.DoesNotExist:
        raise Http404("Activity does not exist")
    return render(request, 'activity/activity_detail.html', {'activity': activity})