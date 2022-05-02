from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.1")

def account(request,id=0):
    return HttpResponse("account returned "+str(id))