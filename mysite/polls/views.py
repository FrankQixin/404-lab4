from django.http import HttpRequest
from django.http.response import HttpResponse
def index(request):
    return HttpResponse("Hello ,World.You are at the polls index")
    
