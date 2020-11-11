import os
import django
import csv
import sys
import bcrypt
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "functionofbeauty.settings")
django.setup()

from user.models import User
from cart.models import Order, OrderStatus, OrderItem
from quiz.models import Quiz, QuizHairGoal, HairGoal, HairType, HairStructure, ScalpMoisture, Fragrance, FragranceStrength
from product.models import Product, ProductTemplate, Color
from review.models import Review

CSV_PATH_USER = "./users.csv"
CSV_PATH_ORDER = "./orders.csv"
CSV_PATH_HAIRGOAL = "./hairgoal.csv"
CSV_PATH_QUIZ = "./quiz.csv"
CSV_PATH_ITEM = "./orderitems.csv"
CSV_PATH_REVIEW = "./review.csv"

#with open(CSV_PATH_USER) as file:
#    data = csv.reader(file)
#    next(data, None)
#    for row in data:
#        first_name = row[0]
#        last_name = row[1]
#        email = row[2]
#        password = row[3]
#        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
#        User.objects.create(first_name=first_name, last_name=last_name, email=email, password=hashed_password)
#
#with open(CSV_PATH_ORDER) as file:
#    data = csv.reader(file)
#    next(data,None)
#    for row in data:
#        user_id = User.objects.get(id=row[0]).id
#        updated_at = datetime.datetime.now()
#        order_number = row[1]
#        order_status_id = OrderStatus.objects.get(id=2)
#        Order.objects.create(user_id=user_id, order_number=order_number, updated_at=updated_at, order_status_id=2)
#
#with open(CSV_PATH_QUIZ) as file:
#    data = csv.reader(file)
#    next(data,None)
#    for row in data:
#        hairtype = HairType.objects.get(id=row[0]).id
#        structure = HairStructure.objects.get(id=row[1]).id
#        moisture = ScalpMoisture.objects.get(id=row[2]).id
#        fragrance = Fragrance.objects.get(id=row[3]).id
#        strength = FragranceStrength.objects.get(id=row[4]).id
#        name = row[5]
#        silicone = row[6]
#        Quiz.objects.create(hair_type_id = hairtype, hair_structure_id=structure, scalp_moisture_id = moisture, fragrance_id = fragrance, fragrance_strength_id = strength, formula_name = name, silicone_free = silicone)
#
#with open(CSV_PATH_HAIRGOAL) as file:
#    data = csv.reader(file)
#    next(data,None)
#    for row in data:
#        quiz_id = Quiz.objects.get(id=row[0]).id
#        hairgoal_id = HairGoal.objects.get(id=row[1]).id
#        QuizHairGoal.objects.create(quiz_id=quiz_id, hair_goal_id=hairgoal_id)
#
#with open(CSV_PATH_ITEM) as file:
#    data = csv.reader(file)
#    next(data, None)
#    for row in data:
#        order_id = Order.objects.get(id=row[0]).id
#        quiz_id = Quiz.objects.get(id=row[1]).id
#        product_id = Product.objects.get(id=row[2]).id if row[2] else None
#        template_id = ProductTemplate.objects.get(id=row[3]).id  if row[3] else None
#        shampoo_color = Color.objects.get(id=row[4]).id if row[4] else None
#        conditioner_color = Color.objects.get(id=row[5]).id if row[5] else None
#        OrderItem.objects.create(order_id=order_id, quiz_id=quiz_id, product_id=product_id, template_id=template_id, shampoo_color=shampoo_color, conditioner_color=conditioner_color)
#
#with open(CSV_PATH_REVIEW) as file:
#    data = csv.reader(file)
#    next(data, None)
#    for row in data:
#        order_item = OrderItem.objects.get(id=row[0])
#        user_id = order_item.order.user_id
#        name = User.objects.get(id=user_id).first_name
#        rating = row[1]
#        title = row[2]
#        comment = row[3]
#        Review.objects.create(order_item_id=order_item.id, user_id=user_id, name=name, rating=rating, title=title, comment=comment)
