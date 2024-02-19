from django.db import models

# Create your models here.
class Businesscategories(models.Model):
    bid = models.AutoField(primary_key=True)
    businesscategory = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'businesscategories'