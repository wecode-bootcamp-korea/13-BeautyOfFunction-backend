from django.test      import TestCase, Client

from quiz.models import (
    HairType,
    HairStructure,
    ScalpMoisture,
    HairGoal,
    Fragrance,
    FragranceStrength,
)
from product.models import (
    Color,
    ProductTemplate,
    CategoryColor,
    Category
)
from user.models import Frequency

client = Client()

class HairProfileTest(TestCase):
    def setUp(self):
        HairType.objects.create(id=1, hair_type="test1")
        HairStructure.objects.create(id=2, hair_structure="test2")
        ScalpMoisture.objects.create(id=3, scalp_moisture="test3")

    def tearDown(self):
        HairType.objects.get(id=1).delete()
        HairStructure.objects.get(id=2).delete()
        ScalpMoisture.objects.get(id=3).delete()

    def test_hair_profile_success(self):
        hair_profile = [{
            'hair_types': [{
                'id'  : 1,
                'type': 'test1'
            }],
            'hair_structures': [{
                'id'       : 2,
                'structure': 'test2'
            }],
            'scalp_moistures': [{
                'id'      : 3,
                'moisture': 'test3'
            }]
        }]

        response = client.get('/quiz/hair-profile')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"hair_profile": hair_profile})

    def test_hair_profile_fail(self):
        response = client.get('/quiz/hairprofile')
        self.assertEqual(response.status_code, 404)

class HairGoalTest(TestCase):
    def setUp(self):
        functions = [
            HairGoal(
                id=i, function=f"test{i}"
            )
            for i in range(1,4)
        ]
        HairGoal.objects.bulk_create(objs=functions)

    def tearDown(self):
        HairGoal.objects.filter(id__lte=3).delete()

    def test_hair_goal_success(self):
        hair_goals = [
            {
                'id': 1,
                'goal': 'test1'
            },
            {
                'id':2,
                'goal': 'test2'
            },
            {
                'id': 3,
                'goal': 'test3'
            }
        ]

        response = client.get('/quiz/hair-goals')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"hair_goals": hair_goals})

    def test_hair_goal_fail(self):
        response = client.get('/quiz/hair-goal')
        self.assertEqual(response.status_code, 404)

class CustomizingTest(TestCase):
    def setUp(self):
        fragrances = [
            Fragrance(
                id=i, fragrance=f"scent{i}", fragrance_image=f"url{i}"
            )
            for i in range(1,5)
        ]
        Fragrance.objects.bulk_create(objs=fragrances)

        FragranceStrength.objects.create(id=1, strength="light")
        FragranceStrength.objects.create(id=2, strength="strong")

        colors = [
            Color(
                id=i, color_code=f"{i}"
            )
            for i in range(1,10)
        ]
        Color.objects.bulk_create(objs=colors)
        Category.objects.create(id=1,name="test",description="test",ingredients_image_url="test",recommended_image_url="test",great_for_image_url="test",ingredients="test",recommended="test",great_for="test",short_description="test")
        images = [
            CategoryColor(
                category_id=1, color_id=i, product_image_url=f"url{i}"
            )
            for i in range(1,10)
        ]
        CategoryColor.objects.bulk_create(objs=images)

    def tearDown(self):
        Color.objects.filter(id__lte=9).delete()
        Fragrance.objects.filter(id__lte=4).delete()
        FragranceStrength.objects.filter(id__lte=2).delete()
        Category.objects.get(id=1).delete()
        CategoryColor.objects.filter(id__lte=9).delete()

    def test_customizing_purple_shampoo_success(self):
        fragrance_options = [
            {
                'fragrances': [
                    {
                        'id': 1,
                        'fragrance': 'scent1',
                        'image': 'url1'
                    },
                    {
                        'id': 2,
                        'fragrance': 'scent2',
                        'image': 'url2'
                    },
                    {
                        'id': 3,
                        'fragrance': 'scent3',
                        'image': 'url3'
                    },
                    {
                        'id': 4,
                        'fragrance': 'scent4',
                        'image': 'url4'
                    }
                ],
                'strengths': [
                    {
                        'id': 1,
                        'strength': 'light'
                    },
                    {
                        'id': 2,
                        'strength': 'strong'
                    }
                ]
            }
        ]
        shampoo_colors = [
            {
                'id': 9,
                'color_code': '9',
                'color_image': 'url9'
            }
        ]

        conditioner_colors = [
            {
                'id': 1,
                'color_code': '1',
                'color_image': 'url1'
            },
            {
                'id': 2,
                'color_code': '2',
                'color_image': 'url2'
            },
            {
                'id': 3,
                'color_code': '3',
                'color_image': 'url3'
            },
            {
                'id': 4,
                'color_code': '4',
                'color_image': 'url4'
            },
            {
                'id': 5,
                'color_code': '5',
                'color_image': 'url5'
            },

            {
                'id': 6,
                'color_code': '6',
                'color_image': 'url6'
            },
            {
                'id': 7,
                'color_code': '7',
                'color_image': 'url7'
            },

            {
                'id': 8,
                'color_code': '8',
                'color_image': 'url8'
            },
        ]
 
        response = client.post('/quiz/appearance-and-fragrance', {"purple_shampoo": True}, content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "fragrance_options" : fragrance_options,
            "shampoo_colors"    : shampoo_colors,
            "conditioner_colors": conditioner_colors
        })

    def test_customizing_normal_shampoo_success(self):
        fragrance_options = [
            {
                'fragrances': [
                    {
                        'id': 1,
                        'fragrance': 'scent1',
                        'image': 'url1'
                    },
                    {
                        'id': 2,
                        'fragrance': 'scent2',
                        'image': 'url2'
                    },
                    {
                        'id': 3,
                        'fragrance': 'scent3',
                        'image': 'url3'
                    },
                    {
                        'id': 4,
                        'fragrance': 'scent4',
                        'image': 'url4'
                    }
                ],
                'strengths': [
                    {
                        'id': 1,
                        'strength': 'light'
                    },
                    {
                        'id': 2,
                        'strength': 'strong'
                    }
                ]
            }
        ]
        shampoo_colors = [
            {
                'id': 1,
                'color_code': '1',
                'color_image': 'url1'
            },
            {
                'id': 2,
                'color_code': '2',
                'color_image': 'url2'
            },
            {
                'id': 3,
                'color_code': '3',
                'color_image': 'url3'
            },
            {
                'id': 4,
                'color_code': '4',
                'color_image': 'url4'
            },
            {
                'id': 5,
                'color_code': '5',
                'color_image': 'url5'
            },

            {
                'id': 6,
                'color_code': '6',
                'color_image': 'url6'
            },
            {
                'id': 7,
                'color_code': '7',
                'color_image': 'url7'
            },

            {
                'id': 8,
                'color_code': '8',
                'color_image': 'url8'
            },
        ]
        conditioner_colors = [
            {
                'id': 1,
                'color_code': '1',
                'color_image': 'url1'
            },
            {
                'id': 2,
                'color_code': '2',
                'color_image': 'url2'
            },
            {
                'id': 3,
                'color_code': '3',
                'color_image': 'url3'
            },
            {
                'id': 4,
                'color_code': '4',
                'color_image': 'url4'
            },
            {
                'id': 5,
                'color_code': '5',
                'color_image': 'url5'
            },

            {
                'id': 6,
                'color_code': '6',
                'color_image': 'url6'
            },
            {
                'id': 7,
                'color_code': '7',
                'color_image': 'url7'
            },

            {
                'id': 8,
                'color_code': '8',
                'color_image': 'url8'
            },
        ]
        response = client.post('/quiz/appearance-and-fragrance', {"purple_shampoo": False}, content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "fragrance_options" : fragrance_options,
            "shampoo_colors"    : shampoo_colors,
            "conditioner_colors": conditioner_colors
        })

#    def test_customizing_key_error(self):
#        response = client.post('/quiz/appearance-and-fragrance', content_type='application/json')
#        self.assertEqual(response.status_code, 400)

#    def test_customizint_fail(self):
#        response = Client.post('/quiz/fragrance-and-appearance', content_type='application/json')
#        self.assertEqual(response.status_code, 404)

