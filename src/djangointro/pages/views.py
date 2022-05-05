from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})


def about(request):
    # info_ = "Welcome, Ikenna"
    from pages.external_module import namer
    return render(request, 'about.html', {"data": namer()})
