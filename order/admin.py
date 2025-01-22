from django.contrib import admin
from .models import Order, CartItems

class CartItemsInline(admin.TabularInline):
    """
    Inline admin to display cart items within the Order admin page.
    """
    model = CartItems
    extra = 0  # Don't show empty extra forms

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'orderstatus', 'get_products', 'get_total_quantity', 'email')
    list_filter = ('orderstatus', 'city', 'place')  # Filters for easier navigation
    search_fields = ('owner__name', 'email', 'city')  # Search by owner name, email, or city
    inlines = [CartItemsInline]

    def get_products(self, obj):
        """
        Display the products associated with this order.
        """
        return ", ".join([f"{item.product.name} (x{item.quantity})" for item in obj.get_cart_items()])

    def get_total_quantity(self, obj):
        """
        Display the total quantity of items in the cart.
        """
        return sum(item.quantity for item in obj.get_cart_items())

    get_products.short_description = 'Ordered Products'
    get_total_quantity.short_description = 'Total Quantity'

# Register models
admin.site.register(Order, OrderAdmin)
