from django.shortcuts import render


def index(request):
    return render(request, "communication/communication.html")
