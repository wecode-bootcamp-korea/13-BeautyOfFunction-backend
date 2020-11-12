import json
import requests

from django.http  import JsonResponse
from django.views import View

from quiz.models import (
    HairType,
    HairStructure,
    ScalpMoisture,
    HairGoal,
    Fragrance,
    FragranceStrength
)
from product.models import (
    Product,
    ProductTemplate,
    Color,
    CategoryColor,
    DetailImage
)
from user.models import Subscription, Frequency
from utils       import query_debugger

class HairProfileView(View):
    def get(self, request):
        hair_types = HairType.objects.all()
        structures = HairStructure.objects.all()
        moistures  = ScalpMoisture.objects.all()

        hair_profile = [{
            'hair_types': [{
                'id'  : hair_type.id,
                'type': hair_type.hair_type
            } for hair_type in hair_types],
            'hair_structures': [{
                'id'       : structure.id,
                'structure': structure.hair_structure
            } for structure in structures],
            'scalp_moistures': [{
                'id'      : moisture.id,
                'moisture': moisture.scalp_moisture
            } for moisture in moistures]
        }]

        return JsonResponse({"hair_profile": hair_profile}, status=200)

class HairGoalView(View):
    def get(self, request):
        goals = HairGoal.objects.all()

        hair_goals = [{
            'id'  : goal.id,
            'goal': goal.function
        } for goal in goals]

        return JsonResponse({"hair_goals": hair_goals}, status=200)

class CustomizingView(View):
    @query_debugger
    def post(self, request):
        try:
            data = json.loads(request.body)
            purple_shampoo = data['purple_shampoo']

            fragrances = Fragrance.objects.all()
            strengths  = FragranceStrength.objects.all()

            fragrance_options = [{
                'fragrances': [{
                    'id'       : fragrance.id,
                    'fragrance': fragrance.fragrance,
                    'image'    : fragrance.fragrance_image
                } for fragrance in fragrances],
                'strengths': [{
                    'id'      : strength.id,
                    'strength': strength.strength
                } for strength in strengths]
            }]

            shampoo_colors     = Color.objects.prefetch_related('categorycolor_set')[:8] if purple_shampoo == False else Color.objects.filter(id=9)
            conditioner_colors = Color.objects.prefetch_related('categorycolor_set')[:8]

            shampoo_colors = [{
                'id'         : color.id,
                'color_code' : color.color_code,
                'color_image': color.categorycolor_set.all()[0].product_image_url
            } for color in shampoo_colors]

            conditioner_colors = [{
                'id'         : color.id,
                'color_code' : color.color_code,
                'color_image': color.categorycolor_set.all()[0].product_image_url
            } for color in conditioner_colors]

            return JsonResponse({
                "fragrance_options" : fragrance_options,
                "shampoo_colors"    : shampoo_colors,
                "conditioner_colors": conditioner_colors
            }, status=200)

        except KeyError:
            return JsonResponse({"Message": "KEY_ERROR"}, status=400)

class ProductOptionView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            shampoo_color_id     = data['shampoo_color']
            conditioner_color_id = data['conditioner_color']

            frequencies = Frequency.objects.all()

            frequency_options = [{
                'id': frequency.id,
                'option': frequency.option
            } for frequency in frequencies]

            product_templates = ProductTemplate.objects.all()
            shampoo_image     = CategoryColor.objects.get(color_id=shampoo_color_id).product_image_url
            conditioner_image = CategoryColor.objects.get(color_id=conditioner_color_id).product_image_url

            size_options = [{
                'shampoo_image'    : shampoo_image,
                'conditioner_image': conditioner_image,
                'size_options': [{
                    'id'   : template.id,
                    'name' : template.name,
                    'price': template.price
                } for template in product_templates]
            }]

            return JsonResponse({
                "size_options"     : size_options,
                "frequency_options": frequency_options
            }, status =200)

        except KeyError:
            return JsonResponse({"Message": "KEY_ERROR"}, status=400)





