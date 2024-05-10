from django.http import HttpResponse

def home_page(request):
    print("home page request")
    return HttpResponse("<center><h1>This is home page</h1></cemter>")