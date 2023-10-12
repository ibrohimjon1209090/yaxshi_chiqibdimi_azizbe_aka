from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *


@api_view(['POST'])
def add_wishlist(request, pk):
    wishlist_name = Room.objects.get(pk=pk)

    saved_wishlist = Wishlist.objects.create(
        user=request.user,
        room = room
    )
    ser = WishlistSerializers(saved_wishlist)
    return Response(ser.data)



@api_view(['PUT'])
def favoured_number(request, pk):
    room = Room.objects.get(pk=pk)
    room.favoured_number += 1
    room.save()
    ser = RoomSerializers(product)
    return Response(ser.data)



@api_view(['GET'])
def get_all_rooms(request):
    room = Room.objects.all()
    ser = RoomSerializers(room, many=True)



@api_view(['GET'])
def filter_room_by_name(request):
    name = request.GET.get('name')
    room = Room.objects.filter(name__icontains=name)
    product = Product.objects.filter(size= size)
    ser = RoomSerializers(room, many=True)
    return Response(ser.data)



@api_view(['GET'])
def search_hotel_by_name(request):
    name = request.GET.get('name')
    hotel = Hotel.objects.filter(name__icontains=name)
    ser = HotelSerializers(hotel, many=True)
    return Response(ser.data)




@api_view(['GET'])
def search_room_by_name(request):
    name = request.GET.get('name')
    brands = Room.objects.filter(name__icontains=name)
    ser = RoomSerializers(brands, many=True)
    return Response(ser.data)




@api_view(['POST'])
def create_comment(request, pk):
    room = Room.objects.get(pk=pk)
    if request.method == "POST":
        text = request.POST['text']
        comment = Comment.objects.create(
            text=text,
            user=request.user,
            room=room
        )
        ser = RoomSerializers(comment)
        return Response(ser.data)



@api_view(['POST'])
def reply_comment(request, pk):
    room = Room.objects.get(pk=pk)
    comment_id = request.POST.get('comment_id')
    text = request.POST['text']
    user = request.user
    new_comment = Comment.objects.create(
        user=user,
        room_id=room,
        text=text,
        comment_id=comment_id,
    )
    ser = CommentSerializers(new_comment)
    return Response(ser.data)



@api_view(['PUT'])
def update_room_like(request, pk):
    room = Room.objects.get(pk=pk)
    room.like_number += 1
    room.save()
    ser = RoomSerializers(product)
    return Response(ser.data)



