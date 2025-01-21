from django.db import models
from customer.models import Customer
from product.models import Products

# Part 2.4 order model
class Order(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'live'),(DELETE,'delete'))
    CART_STAGE=0
    ORDER_PROCESSED=1
    DELIVERED=2
    REJECTED=3
    ORDER_CONFORMED = 4
    STATUS_CHOICE = (
        (ORDER_PROCESSED, "Oroder Processed"),
        (DELIVERED, "DELIVERED"),
        (REJECTED, "REJECTED"),
        (ORDER_CONFORMED, "Order Conformed"),
    )
    orderstatus = models.IntegerField(choices=STATUS_CHOICE, default=0)
    owner=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,related_name='order')
    name=models.CharField(max_length=50,null=False)
    place=models.CharField(max_length=100, null=False)
    address=models.CharField(max_length=100, null=False)
    email=models.EmailField(null=False)
    phonenumber=models.IntegerField(null=False)
    city=models.CharField(max_length=100, null=False)
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)

    def __str__(self) -> str:
        return "orders-{}-{}".format(self.id,self.owner)


# Part 2.3 cart model
class CartItems(models.Model):
    product=models.ForeignKey(Products,related_name='addcart',on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='added')