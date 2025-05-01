from django.shortcuts import render


def chat_view(request):
    return render(request, "chat.html")

def index_view(request):
    return render(request, "base.html")