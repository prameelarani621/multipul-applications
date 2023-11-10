from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def virat(request):
    return render(request,'virat.html')

def ram(request):
    return HttpResponse('ram is a god')