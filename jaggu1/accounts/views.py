from django.shortcuts import render
from django.http import HttpResponse


def about(request):
    return HttpResponse('Hey this is about page')
def contact(request):
    return HttpResponse('Contacting Gaja')
def facilities(request):
    return HttpResponse('our facilties are')
def home(request):
    return render(request,'accounts/index.html')
def dashboard(request):
    return render(request,'accounts/dashboard.html')
def application(request):
    return render(request,'accounts/form.html')
