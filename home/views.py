from django.shortcuts import render

def basepage(request):
    return render(request, 'index.html')

def eventspage(request):
    return render(request, 'eventspage.html')

def teampage(request):
    return render(request, 'teams.html')

def aboutuspage(request):
    return render(request, 'about.html')
