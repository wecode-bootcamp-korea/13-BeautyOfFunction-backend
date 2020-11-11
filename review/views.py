import json

from django.http import JsonResponse
from django.views import View

from cart.models import *
from product.models import *
from .utils import query_debugger

class ReviewView(View):
    def get(self, request):
        product_id = int(request.GET.get("product_id", None))
        offset = int(request.GET.get("offset", 0))
        limit = int(request.GET.get("limit", 5))

        my_filter = {}
        if request.GET.get("hair_type"):
            my_filter.update({"hair_type":int(request.GET.get("hair_type"))})

        if request.GET.get("hair_structure"):
            my_filter.update({"hair_structure":int(request.GET.get("hair_structure"))})

        if request.GET.get("scalp_moisture"):
            my_filter.update({"scalp_moisture":int(request.GET.get("scalp_moisture"))})

        category_id = Product.objects.get(id = product_id).category_id

        if product_id <= 4 :
            order_list = OrderItem.objects.filter(product_id__lte=4).select_related('review','product')

        else :
            order_list = OrderItem.objects.filter(product_id = product_id)

        total_count = order_list.count()
        ratings = [item.review.rating for item in order_list]
        rating_average = round(sum(ratings)/len(ratings),1)


        review_ratings =[{'image' : DetailImage.objects.filter(category_id = category_id)[0].image_url,
                          'total' : order_list.count(),
                          'average' : rating_average,
                          'rating_five' : ratings.count(5),
                          'rating_four' : ratings.count(4),
                          'rating_three' : ratings.count(3),
                          'rating_two' : ratings.count(2),
                          'rating_one' : ratings.count(1)
                         }]


        quiz_id_list = list(Quiz.objects.filter(**my_filter).values_list('id', flat=True))

        order_items = order_list.filter(quiz_id__in = quiz_id_list).select_related('review')

        reviews = [{'name' : order_item.review.name,
                    'rating' : order_item.review.rating,
                    'title' : order_item.review.title,
                    'comment' : order_item.review.comment,
                    'created_at' : order_item.review.created_at.date()
                   }for order_item in order_items][offset:offset+limit]

        return JsonResponse({'review_ratings' : review_ratings, 'reviews' : reviews}, status=200)




