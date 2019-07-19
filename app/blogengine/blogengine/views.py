from django.http import HttpResponse
HttpResponse





def hello(request):
    return HttpResponse('<h1>hello world</h1>')
