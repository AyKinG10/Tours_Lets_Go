from django.shortcuts import render

def tours_home(request):
    return render (request,'tours/news_home.html')