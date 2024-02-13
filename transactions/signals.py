from django.db.models.signals import post_save
from django.dispatch import receiver
from transactions.models import Atransaction, Otransaction, Utransaction

@receiver(post_save, sender=Atransaction)
def update_artistsubsdate(sender, instance, created, **kwargs):
          if created:
                    instance.uid.artistsubsdate = instance.atdate
                    instance.uid.save()

@receiver(post_save, sender=Otransaction)
def update_organizersubsdate(sender, instance, created, **kwargs):
          if created:
                    instance.uid.organizersubsdate = instance.otdate
                    instance.uid.save()

@receiver(post_save, sender=Utransaction)
def update_usersubsdate(sender, instance, created, **kwargs):
          if created:
                            instance.uid.usersubsdate = instance.utdate
                            instance.uid.save()
