from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from orders.models import Order


def take_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if order.status != "waiting":
        return JsonResponse({"success": False, "message": "Order no longer available."})

    order.driver = request.user
    order.status = "assigned"
    order.save()

    return JsonResponse({"success": True, "message": "Order taken!"})

def update_status(request, order_id):
    import json
    body = json.loads(request.body)

    order = get_object_or_404(Order, id=order_id, driver=request.user)

    order.status = body.get("status")
    order.save()

    return JsonResponse({"success": True, "message": "Status updated!"})

# Create your views here.
