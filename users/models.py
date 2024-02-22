from django.db import models
import datetime

# Create your models here.

class User(models.Model):
          uid = models.AutoField(db_column='Uid', primary_key=True)  # Field name made lowercase.
          uname = models.CharField(db_column='Uname', max_length=50, blank=True, null=True,
                                   default=' ')  # Field name made lowercase.
          uemail = models.CharField(db_column='Uemail', max_length=70, blank=True, null=True,
                                    default=' ')  # Field name made lowercase.
          uwhatsappno = models.CharField(db_column='Uwhatsappno', max_length=15, blank=True, null=True,
                                         default=' ')  # Field name made lowercase.
          upassword = models.CharField(db_column='Upassword', max_length=50, blank=True, null=True,
                                       default=' ')  # Field name made lowercase.
          uconfirmpassword = models.CharField(db_column='Uconfirmpassword', max_length=50, blank=True, null=True,
                                              default=' ')  # Field name made lowercase.
          uaddress = models.CharField(db_column='Uaddress', max_length=50, blank=True, null=True,
                                      default=' ')  # Field name made lowercase.
          ucity = models.CharField(db_column='Ucity', max_length=45, blank=True, null=True,
                                   default=' ')  # Field name made lowercase.
          utypeartist = models.IntegerField(db_column='Utypeartist', blank=True, null=True,
                                            default=0)  # Field name made lowercase.
          utypeorganizer = models.IntegerField(db_column='Utypeorganizer', blank=True, null=True,
                                               default=0)  # Field name made lowercase.
          utypeuser = models.IntegerField(db_column='Utypeuser', blank=True, null=True,
                                          default=0)  # Field name made lowercase.
          uregistrationdate = models.DateField(db_column='Uregistrationdate', blank=True, null=True,
                                               default=datetime.date(2024, 1, 1))  # Field name made lowercase.
          userstatus = models.CharField(db_column='Userstatus', max_length=30, blank=True, null=True,
                                        default=' ')  # Field name made lowercase.
          usersubsdate = models.DateField(db_column='Usersubsdate', blank=True, null=True,
                                          default=datetime.date(2024, 1, 1))  # Field name made lowercase.
          ulikes = models.CharField(db_column='Ulikes', max_length=1000, blank=True, null=True,
                                    default='[]')  # Field name made lowercase.
          uwishlist = models.CharField(db_column='Uwishlist', max_length=1000, blank=True, null=True,
                                       default='[]')  # Field name made lowercase.
          aprofilephoto = models.CharField(db_column='Aprofilephoto', max_length=200, blank=True, null=True,
                                           default=' ')  # Field name made lowercase.
          afblink = models.CharField(db_column='Afblink', max_length=200, blank=True, null=True,
                                     default=' ')  # Field name made lowercase.
          ainstalink = models.CharField(db_column='Ainstalink', max_length=200, blank=True, null=True,
                                        default=' ')  # Field name made lowercase.
          awebsite = models.CharField(db_column='Awebsite', max_length=200, blank=True, null=True,
                                      default=' ')  # Field name made lowercase.
          alikes = models.CharField(db_column='Alikes', max_length=1000, blank=True, null=True,
                                    default='[]')  # Field name made lowercase.
          awishlist = models.CharField(db_column='Awishlist', max_length=1000, blank=True, null=True,
                                       default='[]')  # Field name made lowercase.
          acategory = models.CharField(db_column='Acategory', max_length=50, blank=True, null=True,
                                       default=' ')  # Field name made lowercase.
          asubcategory = models.CharField(db_column='Asubcategory', max_length=50, blank=True, null=True,
                                          default=' ')  # Field name made lowercase.
          aworkexperience = models.CharField(db_column='Aworkexperience', max_length=50, blank=True, null=True,
                                             default=' ')  # Field name made lowercase.
          aspeciality = models.CharField(db_column='Aspeciality', max_length=50, blank=True, null=True,
                                         default=' ')  # Field name made lowercase.
          alink1 = models.CharField(db_column='Alink1', max_length=200, blank=True, null=True,
                                    default=' ')  # Field name made lowercase.
          alink2 = models.CharField(db_column='Alink2', max_length=200, blank=True, null=True,
                                    default=' ')  # Field name made lowercase.
          alink3 = models.CharField(db_column='Alink3', max_length=200, blank=True, null=True,
                                    default=' ')  # Field name made lowercase.
          aphotos = models.CharField(db_column='Aphotos', max_length=200, blank=True, null=True,
                                     default=' ')  # Field name made lowercase.
          abookeddate = models.DateField(db_column='Abookeddate', blank=True, null=True,
                                         default=datetime.date(2024, 1, 1))  # Field name made lowercase.
          artistsubsdate = models.DateField(db_column='Artistsubsdate', blank=True, null=True,
                                            default=datetime.date(2024, 1, 1))  # Field name made lowercase.
          arequirements = models.CharField(db_column='Arequirements', max_length=50, blank=True, null=True,
                                           default=' ')  # Field name made lowercase.
          adescription = models.CharField(db_column='Adescription', max_length=500, blank=True, null=True,
                                          default=' ')  # Field name made lowercase.
          artiststatus = models.CharField(db_column='Artiststatus', max_length=30, blank=True, null=True,
                                          default=' ')  # Field name made lowercase.
          oprofilephoto = models.CharField(db_column='Oprofilephoto', max_length=200, blank=True, null=True,
                                           default=' ')  # Field name made lowercase.
          obusinessname = models.CharField(db_column='Obusinessname', max_length=50, blank=True, null=True,
                                           default=' ')  # Field name made lowercase.
          obusinesscategory = models.CharField(db_column='Obusinesscategory', max_length=50, blank=True, null=True,
                                               default=' ')  # Field name made lowercase.
          ofacilities = models.CharField(db_column='Ofacilities', max_length=200, blank=True, null=True,
                                         default=' ')  # Field name made lowercase.
          oinstalink = models.CharField(db_column='Oinstalink', max_length=200, blank=True, null=True,
                                        default=' ')  # Field name made lowercase.
          ofblink = models.CharField(db_column='Ofblink', max_length=200, blank=True, null=True,
                                     default=' ')  # Field name made lowercase.
          owebsite = models.CharField(db_column='Owebsite', max_length=200, blank=True, null=True,
                                      default=' ')  # Field name made lowercase.
          ophotos = models.CharField(db_column='Ophotos', max_length=200, blank=True, null=True,
                                     default=' ')  # Field name made lowercase.
          olikes = models.CharField(db_column='Olikes', max_length=1000, blank=True, null=True,
                                    default='[]')  # Field name made lowercase.
          owishlist = models.CharField(db_column='Owishlist', max_length=1000, blank=True, null=True,
                                       default='[]')  # Field name made lowercase.
          ofacilitesforartist = models.CharField(db_column='Ofacilitesforartist', max_length=200, blank=True, null=True,
                                                 default=' ')  # Field name made lowercase.
          odescription = models.CharField(db_column='Odescription', max_length=500, blank=True, null=True,
                                          default=' ')  # Field name made lowercase.
          organizersubsdate = models.DateField(db_column='Organizersubsdate', blank=True, null=True,
                                               default=datetime.date(2024, 1, 1))  # Field name made lowercase.
          organizerstatus = models.CharField(db_column='Organizerstatus', max_length=30, blank=True, null=True,
                                             default=' ')  # Field name made lowercase.

          class Meta:
                    db_table = 'user'
