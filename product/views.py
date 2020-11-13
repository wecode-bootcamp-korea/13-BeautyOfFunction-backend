import json

from django.http    import HttpResponse
from django.http    import JsonResponse
from django.views   import View

from product.models import Category, DetailImage, Product
from review.models  import Review
from cart.models    import Order,OrderStatus,OrderItem

class CategoriesView(View):

    def get(self, request):

        try :
            categories = Category.objects.all()
 
            item_list = [{
                'category_id' : category.id,
                'image' : category.detailimage_set.all()[0].image_url,
                'name' : category.name,
                'short_info' : category.short_description
            } for category in categories.prefetch_related('detailimage_set')]

            return JsonResponse({'product_list' : item_list}, status=200)

        except Category.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'Category does not exist'}, status=404)


class CategoryView(View):

    def get(self, request, category_id) :

        try :
            item = Category.objects.get(id = category_id)

            result = {
                'image'             : [{"src": detail_image.image_url, 
                                        "id": detail_image.id} 
                                       for detail_image in item.detailimage_set.all()],
                'name'              : "custom"+ " " + item.name,
                'description'       : item.description,
                'ingredients'       : item.ingredients,
                'ingredients_url'   : item.ingredients_image_url,
                'recommended'       : item.recommended,
                'recommended_url'   : item.recommended_image_url,
                'great_for'         : item.great_for,
                'great_for_url'     : item.great_for_image_url
            }

            if category_id == 1 :
                order_list = OrderItem.objects.filter(product_id__lte=4).select_related('review')

            else : 
                product_id = Product.objects.get(category_id = category_id).id
                order_list = OrderItem.objects.filter(product_id = product_id)

            review = [{'name' : item.review.name,
                       'rating' : item.review.rating,
                       'title' : item.review.title,
                       'comment' : item.review.comment,
                       'created_at' : item.review.created_at
                      }for item in order_list]

            return JsonResponse({'detail_list' : result, 
                                 'review_list' : review}, status=200)

        except Category.DoesNotExist :
            return JsonResponse({'MESSAGE' : 'Category does not exist'}, status=400)



