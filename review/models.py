from django.db import models

class Review(models.Model):
    name       = models.CharField(max_length=20)
    rating     = models.IntegerField()
    title      = models.CharField(max_length=45)
    comment    = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    user       = models.ForeignKey('user.User', on_delete=models.CASCADE)

    class Meta:
        db_table = 'reviews'

