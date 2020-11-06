from django.db      import models
from user.models    import User
from product.models import Product, ProductTemplate, Color
from quiz.models    import Quiz

class Order(models.Model):
    user            = models.ForeignKey('user.User', on_delete = models.CASCADE)
    order_number    = models.CharField(max_length = 20, null = True)
    updated_at      = models.DateTimeField(auto_now = True, null = True) 
    order_status    = models.ForeignKey('OrderStatus', on_delete = models.CASCADE)

    class Meta :
        db_table = 'orders'

class OrderStatus(models.Model):
    status = models.CharField(max_length = 20)

    class Meta :
        db_table = 'orders_statuses'

class OrderItem(models.Model):
    order               = models.ForeignKey('Order', on_delete = models.CASCADE)
    quiz                = models.ForeignKey('quiz.Quiz', on_delete = models.CASCADE)
    product             = models.ForeignKey('product.Product', on_delete = models.CASCADE, null = True)
    product_template    = models.ForeignKey('product.ProductTemplate', on_delete = models.CASCADE, null = True)
    shampoo_color       = models.ForeignKey('product.Color', on_delete = models.CASCADE, null = True, related_name = 'shampoo_color')
    conditioner_color   = models.ForeignKey('product.Color', on_delete = models.CASCADE, null = True, related_name = 'conditioner_color')

    class Meta:
        db_table = 'orders_items'
