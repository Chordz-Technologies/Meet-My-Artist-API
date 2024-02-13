from django.db import models
from users.models import User
# Create your models here.

class Atransaction(models.Model):
    atransactionid = models.AutoField(db_column='ATransactionid', primary_key=True)  # Field name made lowercase.
    uid = models.ForeignKey(User, models.DO_NOTHING, db_column='Uid', blank=True, null=True)  # Field name made lowercase.
    atdate = models.DateField(db_column='Atdate', blank=True, null=True)  # Field name made lowercase.
    atamount = models.IntegerField(db_column='Atamount', blank=True, null=True)  # Field name made lowercase.
    atdescription = models.CharField(db_column='Atdescription', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'atransaction'

class Otransaction(models.Model):
    otransactionid = models.AutoField(db_column='OTransactionid', primary_key=True)  # Field name made lowercase.
    uid = models.ForeignKey(User, models.DO_NOTHING, db_column='Uid', blank=True, null=True)  # Field name made lowercase.
    otdate = models.DateField(db_column='Otdate', blank=True, null=True)  # Field name made lowercase.
    otamount = models.IntegerField(db_column='Otamount', blank=True, null=True)  # Field name made lowercase.
    otdescription = models.CharField(db_column='Otdescription', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'otransaction'

class Utransaction(models.Model):
    utransactionid = models.AutoField(db_column='UTransactionid', primary_key=True)  # Field name made lowercase.
    uid = models.ForeignKey(User, models.DO_NOTHING, db_column='Uid', blank=True, null=True)  # Field name made lowercase.
    utdate = models.DateField(db_column='Utdate', blank=True, null=True)  # Field name made lowercase.
    utamount = models.IntegerField(db_column='Utamount', blank=True, null=True)  # Field name made lowercase.
    utdescription = models.CharField(db_column='Utdescription', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'utransaction'