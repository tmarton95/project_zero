from datetime import datetime
import random
from gallery.models import Category

def create_gallery(num=10):
    photo_list = []

    categories = Category.objects.all()
    for index in range(num):
        photo_list.append(
            {
                "pk": index,
                "title": "Photo Title",
                "image": f'https://source.unsplash.com/500x500/?nature,water{index}',
                "comment": "Egyszer volt hol nem volt...",
                "uploaded": datetime.now(),
                "category": random.choice(categories)
            }
        )
    return photo_list
