from django.db import models
from users.models import User

# Create your models here.

class Events(models.Model):
          eid = models.AutoField(db_column='Eid', primary_key=True)
          uid = models.ForeignKey(User, models.DO_NOTHING, db_column='Uid', blank=True, null=True)
          ename = models.CharField(db_column='Ename', max_length=100, blank=True, null=True)
          elocation = models.CharField(db_column='Elocation', max_length=5000, blank=True, null=True)
          edate = models.DateField(db_column='Edate', blank=True, null=True)
          etime = models.TimeField(db_column='Etime', blank=True, null=True)
          eposter = models.CharField(db_column='Eposter', max_length=200, blank=True, null=True)
          uname = models.ForeignKey(User, models.DO_NOTHING, db_column='Uname', related_name='events_uname_set',
                                    blank=True, null=True)
          obusinessname = models.ForeignKey(User, models.DO_NOTHING, db_column='Obusinessname',
                                            related_name='events_obusinessname_set', blank=True, null=True)
          orequirements = models.CharField(db_column='Orequirements', max_length=200, blank=True, null=True)
          erequirements = models.IntegerField(db_column='Erequirements', blank=True, null=True)
          artistequipwith = models.CharField(db_column='Artistequipwith', max_length=100, blank=True, null=True)
          facilitiesforartist = models.CharField(db_column='Facilitiesforartist', max_length=100, blank=True, null=True)

          class Meta:
                    db_table = 'events'
