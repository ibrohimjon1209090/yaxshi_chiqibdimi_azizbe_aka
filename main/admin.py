from django.contrib import admin
from . import models
from models import *



admin.site.register(User)
admin.site.register(Location)
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Book)
admin.site.register(Wishlist)
admin.site.register(HotelImage)
admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Comment)
admin.site.register(Tag)
