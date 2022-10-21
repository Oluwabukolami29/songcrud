from django.http import HttpResponse

# Create your views
def index(request):
    return HttpResponse("Welcome to my music app")
