from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request, 'dashboard/home.html')
    # return HttpResponse('<h1>Home page</h1>')
