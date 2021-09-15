from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("hello world")

def teste(request):
    return HttpResponse("teste")