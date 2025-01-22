from django.db import models
from customer.models import Customer
from product.models import Products

# Part 2.4 order model
class Order(models.Model):
    CART_STAGE = 0
    ORDER_PROCESSED = 1
    DELIVERED = 2
    REJECTED = 3
    ORDER_CONFORMED = 4

    STATUS_CHOICE = (
        (ORDER_PROCESSED, "Order Processed"),
        (DELIVERED, "Delivered"),
        (REJECTED, "Rejected"),
        (ORDER_CONFORMED, "Order Confirmed"),
    )
    
    orderstatus = models.IntegerField(choices=STATUS_CHOICE, default=CART_STAGE)
    owner = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name='order')
    # Order form
    name = models.CharField(max_length=50, null=False)
    place = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False)
    phonenumber = models.IntegerField(default=9999999999)
    city = models.CharField(max_length=100, null=False)

    def __str__(self) -> str:
        return f"Order #{self.id} - {self.owner}"

    def get_cart_items(self):
        """
        Returns all cart items associated with this order.
        """
        return self.added.all()

    def get_cart_products(self):
        """
        Returns a list of all product names in the cart for this order.
        """
        return [item.product.name for item in self.get_cart_items()]
    

class CartItems(models.Model):
    product = models.ForeignKey(Products, related_name='addcart', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    owner = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='added')

    def __str__(self):
        return f"{self.quantity} x {self.product.name} (Order #{self.owner.id})"
