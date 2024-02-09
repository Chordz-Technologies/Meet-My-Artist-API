from django.db import models

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