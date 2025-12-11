# drivers/urls.py
from django.urls import path
from . import views # atau dari mana pun view dashboard driver berada

app_name = 'drivers' # <--- TAMBAHKAN BARIS INI

urlpatterns = [
    path("dashboard/", views.driver_dashboard, name="driver_dashboard"),


    # path("take-order/<int:order_id>/", views.take_order, name="take_order"),
    # path("update-status/<int:order_id>/", views.update_status, name="update_status"),
    path("driver/orders/available/", views.driver_available_orders, name="driver_available_orders"),
    path("driver/orders/my/", views.driver_my_orders, name="driver_my_orders"),
    path("driver/orders/<int:order_id>/accept/", views.driver_accept_order, name="driver_accept_order"),
    path("driver/orders/<int:order_id>/update/", views.driver_update_status, name="driver_update_order"),
    path("driver/history/", views.driver_history, name="driver_history"),
]