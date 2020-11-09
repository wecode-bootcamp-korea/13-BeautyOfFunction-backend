from django.test import TestCase, Client
from product.models import Category, DetailImage

from unittest.mock import patch, MagicMock

client = Client()

class MainTest(TestCase):

    def setUp(self):
        Category.objects.create(
            id = 1,
            name = 'shampoo',
            short_description = 'It is shampoo.',
            description = 'god shampoo.',
            ingredients_image_url  = 'www.ingredients.com',
            recommended_image_url = 'www.recommended.com',
            great_for_image_url = 'www.great_for.com',
            ingredients = 'god.',
            recommended = 'god god.',
            great_for = 'god god god.'
        )

        DetailImage.objects.create(
            id = 1,
            category_id = 1,
            image_url = 'www.detail.com'
        )

    def tearDown(self):
        Category.objects.all().delete()
        DetailImage.objects.all().delete()

    def test_products_get_success(self):
        response = client.get('/products')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json(),{'product_list'
                                          : [{'product_id': 1, 
                                              'image': 'www.detail.com', 
                                              'name': 'shampoo', 
                                              'short_info': 'It is shampoo.'}]})

    def test_products_get_not_found(self):
        response =client.get('/product')
        self.assertEqual(response.status_code,404)
        #self.assertEqual(response.json(),{'MESSAGE' : 'Category does not exist'}, status=404)



class DetailTest(TestCase):

    def setUp(self):
        Category.objects.create(
            id = 1,
            name = 'shampoo',
            short_description = 'It is shampoo.',
            description = 'god shampoo.',
            ingredients_image_url  = 'www.ingredients.com',
            recommended_image_url = 'www.recommended.com',
            great_for_image_url = 'www.great_for.com',
            ingredients = 'god.',
            recommended = 'god god.',
            great_for = 'god god god.'
        )

        DetailImage.objects.create(
            id = 1,
            category_id = 1,
            image_url = 'www.detail.com'
        )

    def tearDown(self):
        Category.objects.all().delete()
        DetailImage.objects.all().delete()

    def test_product_get_success(self):
        response = client.get('/products/1')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json(),{'detail_list': 
                                          {'image': [{'src': 'www.detail.com', 'id': 1}], 
                                           'name': 'customshampoo', 
                                           'description': 'god shampoo.', 
                                           'ingredients': 'god.', 
                                           'ingredients_url': 'www.ingredients.com', 
                                           'recommended': 'god god.', 
                                           'recommended_url': 'www.recommended.com', 
                                           'great_for': 'god god god.', 
                                           'great_for_url': 'www.great_for.com'}})

    def test_product_get_fail(self):
        response = client.get('product/1')
        self.assertEqual(response.status_code,404)




