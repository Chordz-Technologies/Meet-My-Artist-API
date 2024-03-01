from django.db import models

# Create your models here.
# def product_image_path(instance, filename):
#           # Construct the file path
#           return f'Product_Photos/product_{instance.pid}.png'

class Products(models.Model):
          pid = models.AutoField(db_column='Pid', primary_key=True)  # Field name made lowercase.
          pbrand = models.CharField(db_column='Pbrand', max_length=40, blank=True,
                                    null=True)  # Field name made lowercase.
          pmodel = models.CharField(db_column='Pmodel', max_length=100, blank=True,
                                    null=True)  # Field name made lowercase.
          pprice = models.CharField(db_column='Pprice', max_length=50, blank=True,
                                    null=True)  # Field name made lowercase.
          pimages = models.ImageField(db_column='Pimages', max_length=300, blank=True,
                                      null=True)  # Field name made lowercase.

          class Meta:
                    db_table = 'products'
