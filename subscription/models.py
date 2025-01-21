from django.db import models
from users.models import User

# Create your models here.

class Subscription(models.Model):
          sid = models.AutoField(primary_key=True)
          sname = models.CharField(max_length=145, blank=True, null=True)
          sprice = models.CharField(max_length=50, blank=True, null=True)
          sduration = models.IntegerField(blank=True, null=True)
          planfor = models.CharField(max_length=50, blank=True, null=True)
          sbenefits = models.CharField(max_length=500, blank=True, null=True)
          sbenefitsmuted = models.CharField(max_length=500, blank=True, null=True)

          class Meta:
                    db_table = 'subscription'

class Payment(models.Model):
          subscription = models.ForeignKey('Subscription', on_delete=models.CASCADE,
                                           related_name='payments')  # Link to the subscription
          razorpay_order_id = models.CharField(max_length=255)  # Razorpay order ID
          razorpay_payment_id = models.CharField(max_length=255)  # Razorpay payment ID
          amount = models.DecimalField(max_digits=10, decimal_places=2)  # Payment amount (in INR)
          currency = models.CharField(max_length=10, default='INR')  # Currency
          payment_status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed'),
                                                                    ('failed', 'Failed')], default='pending')
          payment_date = models.DateTimeField(auto_now_add=True)  # Timestamp when the payment was made

          class Meta:
                    db_table = 'payments'  # Optional: explicitly define the table name

          def __str__(self):
                    return f"Payment by {self.user.username} for {self.subscription.sname} - {self.payment_status}"
