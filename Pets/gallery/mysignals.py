from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from gallery.models import Owner
from django.contrib.auth.signals import user_logged_in
from gallery.myctxproc import set_st
# from college.myctxproc import set_st

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        Owner.objects.create(user=instance, name=instance.username)
#JAB USER SIGN UP KREGA TOH APNE AAP USKI PROFILE BAN JAEGI
def do_stuff(sender, user, request, **kwargs): #STUDENT KI DETAILS LA RHA H
    if user.is_staff:
        st=None
    else:    
        st = Owner.objects.filter(user=request.user.id)[0] 
    set_st(st)
user_logged_in.connect(do_stuff)