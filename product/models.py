from django.db import models

class Category(models.Model):
    name                    = models.CharField(max_length = 45)
    description             = models.TextField()
    ingredients_image_url   = models.URLField(max_length = 2000)
    recommended_image_url   = models.URLField(max_length = 2000)
    great_for_image_url     = models.URLField(max_length = 2000)
    ingredients             = models.CharField(max_length = 300)
    recommended             = models.CharField(max_length = 300)
    great_for               = models.CharField(max_length = 300)

    class Meta :
        db_table = 'categories'

class DetailImage(models.Model):
    category        = models.ForeignKey('Category', on_delete = models.CASCADE)
    image_url       = models.URLField(max_length = 2000)

    class Meta :
        db_table = 'detail_images'

class Product(models.Model):
    name        = models.CharField(max_length = 45)
    price       = models.DecimalField(max_digits = 10, decimal_places = 2, null=True)
    size        = models.DecimalField(max_digits = 10, decimal_places = 2)
    category    = models.ForeignKey('Category', on_delete = models.CASCADE)
    color       = models.ManyToManyField('Color', through = 'ProductColor')

    class Meta :
        db_table = 'products'

class ProductTemplate(models.Model):
    name        = models.CharField(max_length = 45)
    price       = models.DecimalField(max_digits = 10, decimal_places = 2)
    shampoo     = models.ForeignKey('Product', on_delete = models.CASCADE, null = True, related_name = 'shampoo')
    conditioner = models.ForeignKey('Product', on_delete = models.CASCADE, null = True, related_name = 'conditioner')

    class Meta :
        db_table = 'product_templates'

class Color(models.Model):
    color_code = models.CharField(max_length = 10)

    class Meta :
        db_table = 'colors'

class ProductColor(models.Model):
    product             = models.ForeignKey('Product', on_delete = models.CASCADE)
    color               = models.ForeignKey('Color', on_delete = models.CASCADE, null = True)
    product_image_url   = models.URLField(max_length = 2000)

    class Meta :
        db_table = 'product_images'



