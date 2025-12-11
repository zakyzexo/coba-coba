from django.urls import path
from . import views

app_name = 'restaurants'

urlpatterns = [
    path('', views.restaurant_list, name='list'),
    path('create/', views.restaurant_create, name='create'),

    path('<int:id>/edit/', views.restaurant_edit, name='edit'),
    path('<int:id>/delete/', views.restaurant_delete, name='delete'),

    # menu
    path('<int:resto_id>/menus/', views.menu_list, name='menu_list'),
    path('<int:resto_id>/menus/create/', views.menu_create, name='menu_create'),
    path('<int:resto_id>/menus/<int:id>/edit/', views.menu_edit, name='menu_edit'),
    path('<int:resto_id>/menus/<int:id>/delete/', views.menu_delete, name='menu_delete'),
]
