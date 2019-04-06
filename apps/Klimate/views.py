from django.shortcuts import render, redirect

def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")
def one_method(request):                # no values passed via URL
    pass  