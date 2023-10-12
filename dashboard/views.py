from main.models import Order, Product
from main.serializers import *
from rest_framework.decorators import api_view
from  rest_framework.response import Response


@api_view(['POST'])
def create_room(request):
    if request.method == "POST":
        name = request.POST.get('name')
        hotel = request.POST.get('hotel')
        photo = request.POST.getlist('photo')
        price = request.POST.get('price')
        bonus = request.POST.get('bonus')
        tags = request.POST.getlist('tags')
        description = request.POST.get('description')
        creadit = request.POST.get('credit')
        rank = request.POST.get('rank')
        favoured = request.POST.get('favoured')
        is_active = request.POST.get('is_active')
        is_sale = request.POST.get('is_sale')
        sale = request.POST.get('sale')
        description = request.POST.get('description')
        extant = request.POST.get('extant')
        like_number = request.POST.get('like_number')
        new_room = Product.objects.create(
            name=name,
            price=price,











