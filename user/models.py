from django.db          import models
from creditcards.models import CardNumberField, CardExpiryField

class User(models.Model):
    email          = models.EmailField(max_length=254, unique=True)
    password       = models.CharField(max_length=1000)
    first_name     = models.CharField(max_length=45, null=True)
    last_name      = models.CharField(max_length=45, null=True)
    address1       = models.CharField(max_length=45, null=True)
    address2       = models.CharField(max_length=45, null=True)
    country        = models.CharField(max_length=45, null=True)
    city           = models.CharField(max_length=45, null=True)
    state_province = models.CharField(max_length=45, null=True)
    zip_code       = models.IntegerField(null=True)
    phone_number   = models.CharField(max_length=20, null=True)
    created_at     = models.DateField(auto_now_add=True)
    updated_at     = models.DateField(null=True)

    class Meta:
        db_table = 'users'

class PaymentMethod(models.Model):
    user      = models.ForeignKey('User', on_delete=models.CASCADE)
    cc_number = CardNumberField('card number')
    cc_expiry = CardExpiryField('expiration date')

    class Meta:
        db_table = 'paymentmethods'

class Subscription(models.Model):
    user               = models.ForeignKey('User', on_delete=models.CASCADE)
    frequency          = models.ForeignKey('Frequency', on_delete=models.CASCADE)
    start_date         = models.DateField(auto_now_add=True)
    next_delevery_date = models.DateField()
    order              = models.ForeignKey('cart.Order', on_delete=models.CASCADE)

    class Meta:
        db_table = 'subscriptions'

class Frequency(models.Model):
    option         = models.CharField(max_length=20)
    number_of_days = models.IntegerField(default=0)

    class Meta:
        db_table = 'frequencies'
