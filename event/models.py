from django.db import models
from users.models import User

# Create your models here.

class Events(models.Model):
          eid = models.AutoField(db_column='Eid', primary_key=True)  # Field name made lowercase.
          uid = models.ForeignKey(User, models.DO_NOTHING, db_column='Uid', blank=True,
                                  null=True)  # Field name made lowercase.
          ename = models.CharField(db_column='Ename', max_length=100, blank=True,
                                   null=True)  # Field name made lowercase.
          elocation = models.CharField(db_column='Elocation', max_length=100, blank=True,
                                       null=True)  # Field name made lowercase.
          egooglemap = models.CharField(db_column='Egooglemap', max_length=5000, blank=True,
                                        null=True)  # Field name made lowercase.
          edate = models.DateField(db_column='Edate', blank=True, null=True)  # Field name made lowercase.
          etime = models.TimeField(db_column='Etime', blank=True, null=True)  # Field name made lowercase.
          eposter = models.CharField(db_column='Eposter', max_length=200, blank=True,
                                     null=True)  # Field name made lowercase.
          orequirements = models.CharField(db_column='Orequirements', max_length=200, blank=True,
                                           null=True)  # Field name made lowercase.
          erequirements = models.IntegerField(db_column='Erequirements', blank=True,
                                              null=True)  # Field name made lowercase.
          artistequipwith = models.CharField(db_column='Artistequipwith', max_length=100, blank=True,
                                             null=True)  # Field name made lowercase.
          facilitiesforartist = models.CharField(db_column='Facilitiesforartist', max_length=100, blank=True,
                                                 null=True)  # Field name made lowercase.
          uname = models.CharField(db_column='Uname', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.
          obusinessname = models.CharField(db_column='Obusinessname', max_length=50, blank=True,
                                           null=True)  # Field name made lowercase.

          class Meta:
                    db_table = 'events'
