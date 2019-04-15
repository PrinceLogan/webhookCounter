from django.shortcuts import render
import json, copy, datetime
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from .models import WebhookTransaction, PackageString
from webhookProcessor import take_latest

# Create your views here.
def index(request):
    counter_green = PackageString.objects.filter(source='green').count()
    counter_red = PackageString.objects.filter(source='red').count()
    context1 = {'counter_green': counter_green, 'counter_red': counter_red}
    #context2 = {'counter_red': counter_red}
    return render(request, 'index.html', context1)

@csrf_exempt
@require_POST
def reciever(request):
    jsondata = request.body
    data = json.loads(jsondata)
    meta = copy.copy(request.META)
    WebhookTransaction.objects.create(
        body=data
    )
    take_latest()
    return HttpResponse(status=200)
