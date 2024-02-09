from django.db import models

# Create your models here.
class Artistcategories(models.Model):
    cid = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=70, blank=True, null=True)
    scname = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'artistcategories'