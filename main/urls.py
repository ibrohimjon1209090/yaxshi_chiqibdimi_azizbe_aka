from django.urls import path
from . import views


urlpatterns =[
    path('get-all-rooms/', views.get_all_rooms),
    path('filter-room-by-name/', views.filter_room_by_name),
    path('search-hotel-by-name/', views.search_hotel_by_name),
    path('search-room-by-name/', views.search_room_by_name),
    path('add-liked/<int:pk>/', views.add_wishlist),
    path('create_comment/<int:pk>/', views.create_comment),
    path('update-products-like/<int:pk>/', views.update_room_like)
]