from django.http import HttpResponse
from django.shortcuts import render

data={
    'title' :'Book kingdom',
    'deta' : 'Welcome Everyone',
    'list' : ['Python', 'Django'],
    'num' : [110, 30, 50, 11, 100],
    's_details' : [
        {'name': 'Sabal', 'phone':'901891010'},
        {'name': 'Sam', 'phone':'901091110'}
    ]
}  

def homepage(request):
    return render(request, "home.html",data)

def login(request):
    return render (request, "Login.html")

def catalogue(request):
    return render (request, "catalogue.html")

def form(request):
    return render (request, "form.html")