from rest_framework import serializers
from .models import *




class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"



class HotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = "__all__"





class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Room
        fields = "__all__"


class WishlistSerializers(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = "__all__"



class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"




class HotelImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = "__all__"



class LocationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class Sub_CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Sub_Category
        fields = "__all__"
