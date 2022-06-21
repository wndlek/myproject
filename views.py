from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')
def result(request):
    return render(request, '1.html')
def a(request):
    return render(request, 'a.html')
def b(request):
    return render(request, 'b.html')
def c(request):
    return render(request, 'c.html')
