from django.shortcuts import render

from .models import Category
from utilities.gallery_generator import create_gallery

# template function for creating random images
photos = create_gallery(num=10)

def gallery(request):
    photos_list = [i for i in photos]

    category = request.GET.get("category")
    if category:
        photos_list = [i for i in photos if i["category"].title == category]

    context = {
        "categories": Category.objects.all(),
        "photos": photos_list
    }
    return render(request, 'gallery.html', context)

def photo_details_view(request, pk):
    photo = [i for i in photos if i["pk"] == pk][0]
    return render(request, 'photo_details.html', {"photo": photo})