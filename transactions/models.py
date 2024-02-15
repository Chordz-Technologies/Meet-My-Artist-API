from django.db import models
from users.models import User
from subscription.models import Subscription
# Create your models here.

class Atransaction(models.Model):
    atransactionid = models.AutoField(db_column='ATransactionid', primary_key=True)  # Field name made lowercase.
    uid = models.ForeignKey(User, models.DO_NOTHING, db_column='Uid', blank=True, null=True)  # Field name made lowercase.
    sid = models.ForeignKey(Subscription, models.DO_NOTHING, db_column='sid', blank=True, null=True)
    atdate = models.DateField(db_column='Atdate', blank=True, null=True)  # Field name made lowercase.
    atamount = models.CharField(db_column='Atamount', max_length=300, blank=True, null=True)  # Field name made lowercase.
    atdescription = models.CharField(db_column='Atdescription', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'atransaction'

class Otransaction(models.Model):
    otransactionid = models.AutoField(db_column='OTransactionid', primary_key=True)  # Field name made lowercase.
    uid = models.ForeignKey(User, models.DO_NOTHING, db_column='Uid', blank=True, null=True)  # Field name made lowercase.
    sid = models.ForeignKey(Subscription, models.DO_NOTHING, db_column='sid', blank=True, null=True)
    otdate = models.DateField(db_column='Otdate', blank=True, null=True)  # Field name made lowercase.
    otamount = models.CharField(db_column='Otamount', max_length=300, blank=True, null=True)  # Field name made lowercase.
    otdescription = models.CharField(db_column='Otdescription', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'otransaction'

class Utransaction(models.Model):
    utransactionid = models.AutoField(db_column='UTransactionid', primary_key=True)  # Field name made lowercase.
    uid = models.ForeignKey(User, models.DO_NOTHING, db_column='Uid', blank=True, null=True)  # Field name made lowercase.
    sid = models.ForeignKey(Subscription, models.DO_NOTHING, db_column='sid', blank=True, null=True)
    utdate = models.DateField(db_column='Utdate', blank=True, null=True)  # Field name made lowercase.
    utamount = models.CharField(db_column='Utamount', max_length=300, blank=True, null=True)  # Field name made lowercase.
    utdescription = models.CharField(db_column='Utdescription', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'utransaction'