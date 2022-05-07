from django.shortcuts import render


def index(request):
    template = 'online_service/index.html'
    return render(request, template)
