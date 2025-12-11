from django.db import models
from accounts.models import User

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('preparing', 'Preparing'),
        ('delivering', 'Delivering'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    customer = models.ForeignKey(
        'accounts.User', 
        on_delete=models.CASCADE, 
        related_name='customer_orders',
        limit_choices_to={'role': 'customer'}
    )
    restaurant = models.ForeignKey(
        'accounts.User', 
        on_delete=models.CASCADE, 
        related_name='restaurant_orders',
        limit_choices_to={'role': 'restaurant'}
    )
    driver = models.ForeignKey(
        'accounts.User', 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL,
        related_name='driver_orders',
        limit_choices_to={'role': 'driver'}
    )
    
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    delivery_address = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Order #{self.id} - {self.customer.username} from {self.restaurant.username}"
    
    def is_active(self):
        """Check if order is still active (not completed or cancelled)"""
        return self.status not in ['completed', 'cancelled']


class OrderItem(models.Model):
    """Items dalam order"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    item_name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.quantity}x {self.item_name}"
    
    def subtotal(self):
        return self.quantity * self.price
