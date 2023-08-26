from django.db.models.signals import post_save,post_delete

from django.dispatch import receiver
from .models import Follow
from Account.models import *



@receiver(post_save,sender=Follow)
def update_follow_counts(sender,instane,created,**kwargs):
    if created:
        followed_user=instane.followed_user
        following_user=instane.following_user

        followed_user_profile=User.objects.get(user=followed_user)
        followed_user_profile.followers_count +=1
        followed_user_profile.save()


        following_user_profile=User.objects.get(user=following_user)
        following_user_profile.following_count +=1
        following_user_profile.save()


@ receiver(post_delete,sender=Follow)
def udpate_follow_count_on_delete(sender,instance,**kwargs):
    followed_user=instance.followed_user
    following_user=instance.following_user


    followed_user_profile=User.objects.get(user=followed_user)
    followed_user_profile.followers_count -=1
    followed_user_profile.save()

    
    following_user_profile=User.objects.get(user=following_user)
    following_user_profile.following_count -=1
    following_user_profile.save()



    