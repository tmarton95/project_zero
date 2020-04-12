from django.shortcuts import render, HttpResponse

from .models import HomeMessage

def home(request):
    message_object = HomeMessage.objects.all()

    if message_object:
        message_object = message_object[0]

    context = {
        "object": message_object
        #"title": "Welcome on my page!",
        #"message": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusantium adipisci aspernatur consequuntur corporis deleniti .",
        #"image": "https://source.unsplash.com/1600x900/?nature,water"
    }

    return render(request, 'home.html', context)

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')