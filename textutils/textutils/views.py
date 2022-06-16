# this site is created by Joel
from django.http import HttpResponse

INTROobject = open(r"D:\Coding\DjangoProject\textutils\Intro.txt","r")
content = INTROobject.read()
INTROobject.close()

def index(request):
    return HttpResponse(content)

def about(request):
    return HttpResponse('Just the first proper tutorial done')

def next(request):
    return HttpResponse('Gonna watch the next tutorial')