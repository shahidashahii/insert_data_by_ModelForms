from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

def insert_topic(request):
    TFO=TopicForm()
    d={'TFO':TFO}
    if request.method=='POST':
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('Data is inserted succesffully')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    WFO=webpageForm()
    d={'WFO':WFO}

    if request.method=='POST':
        WFD=webpageForm(request.POST)
        if WFD.is_valid():
            TDF.save()
            return HttpResponse('Data inserted successfully')
    return render(request,'insert_webpage.html',d)

def insert_accessrecord(request):
    AFO=AccessRecordForm()
    d={'AFO':AFO}
    if request.method=='POST':
        AFD=AccessRecordForm(request.POST)
        if AFD.is_valid():
            AFD.save()
            return HttpResponse('Data inseted succesffully')

    return render(request,'insert_accessrecord.html',d)