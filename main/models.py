from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=30)
    phone  = models.CharField(max_length=13, unique=True, blank=True, null=True)
    avatar = models.ImageField(upload_to='user_avatar', blank=True, null=True)



    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'



class Location(models.Model):
    name = models.CharField(max_length=30)





class Hotel(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    room_number = models.IntegerField(max_length=10)
    location = models.ForeignKey(to=Location, on_delete=models.CASCADE)
    rating = models.CharField(max_length=30)






class Room(models.Model):
    hotel = models.ForeignKey(to=Hotel, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    photo = models.ManyToManyField(to='ProductImage', blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=3)
    bonus = models.IntegerField(default=5)
    credit = models.BooleanField(default=False)
    tags = models.ManyToManyField(to='Tag')
    description = models.TextField()
    rank = models.IntegerField(default=0)
    favoured = models.IntegerField(default=0)
    sub_category = models.ForeignKey(to='Sub_Category', on_delete=models.PROTECT)
    extant = models.BooleanField(default=False)
    status = models.IntegerField(default = 2,choices=
    (
        (1,"Band"),
        (2,"Free"),

    )
    )


class Book(models.Model):
    room = models.ManyToManyField(to=Room)
    user = models.ForeignKey(to=User, blank=False, verbose_name="Shopper", on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13)





class Wishlist(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE, verbose_name='Xona')

    def __str__(self):
        return self.room.name




class HotelImage(models.Model):
    image = models.ImageField(upload_to='hotel_images/')



class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Sub_Category(models.Model):
    name = models.CharField(max_length=25)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField(verbose_name='izohlar')
    comment = models.ForeignKey(to='Comment', on_delete=models.CASCADE, null=True, blank=True, related_name='reply')
    date = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)



class Tag(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name


