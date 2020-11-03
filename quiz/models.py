from django.db import models

class Quiz(models.Model):
    hair_type      = models.ForeignKey('HairType', on_delete=models.CASCADE)
    hair_structure = models.ForeignKey('HairStructure', on_delete=models.CASCADE)
    scalp_moisture = models.ForeignKey('ScalpMoisture', on_delete=models.CASCADE)
    fragrance      = models.ForeignKey('Fragrance', on_delete=models.CASCADE)
    formula_name   = models.CharField(max_length=10)

    class Meta:
        db_table = 'quizzes'

class HairType(models.Model):
    hair_type = models.CharField(max_length=10)

    class Meta:
        db_table = 'hair_types'

class HairStructure(models.Model):
    hair_structure = models.CharField(max_length=10)

    class Meta:
        db_table = 'hair_structures'

class ScalpMoisture(models.Model):
    scalp_moisture = models.CharField(max_length=10)

    class Meta:
        db_table = 'scalp_moistures'

class HairGoal(models.Model):
    function      = models.CharField(max_length=20)
    silicone_free = models.BooleanField(default=False)
    quiz          = models.ManyToManyField('Quiz', through='QuizHairGoal')

    class Meta:
        db_table = 'hair_goals'

class QuizHairGoal(models.Model):
    quiz      = models.ForeignKey('Quiz', on_delete=models.CASCADE)
    hair_goal = models.ForeignKey('HairGoal', on_delete=models.CASCADE)

    class Meta:
        db_table = 'quizzes_hair_goals'

class Fragrance(models.Model):
    fragrance          = models.CharField(max_length=30)
    fragrance_image    = models.URLField(max_length=1000)
    fragrance_strength = models.ForeignKey('FragranceStrength', on_delete=models.CASCADE)

    class Meta:
        db_table = 'fragrances'

class FragranceStrength(models.Model):
    strength = models.CharField(max_length=10)

    class Meta:
        db_table = 'fragrance_strengths'

