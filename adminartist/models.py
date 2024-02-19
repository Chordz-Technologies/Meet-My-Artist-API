from django.db import models

# Create your models here.
class Adminartist(models.Model):
    aid = models.AutoField(primary_key=True)
    aname = models.CharField(max_length=50, blank=True, null=True)
    apssword = models.CharField(max_length=50, blank=True, null=True)
    aconfirmpassword = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'adminartist'