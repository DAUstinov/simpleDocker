from django.shortcuts import render

def index(request):
    return render(request, 'hello/index.html')

def secondPage(request):
    return render(request, 'hello/index2.html')

def thirdPage(request):
    return render(request,'hello/ThirdPage.html')

def about(request):
    return render(request, 'hello/about.html')

def contact(request):
    return render(request, 'hello/contact.html')

def news(request):
    return render(request, 'hello/news.html')