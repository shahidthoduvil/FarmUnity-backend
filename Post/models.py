from django.db import models
from Account.models import User
from django.db.models import F
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
# Create your models here.

class Post(models.Model):
    image=models.ImageField(upload_to="post_img/",null=True,blank=True)
    title=models.CharField(max_length=100,null=True)
    description=models.TextField(blank=True)
    date=models.DateTimeField(auto_now_add=True)
    like_count=models.PositiveIntegerField(default=0)
    comment_count=models.PositiveIntegerField(default=0)
    Location=models.CharField(max_length=100,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True)

    class Meta:
       verbose_name='Post'

    def __str__(self):
       return self.title


class Comments(models.Model):
    comment=models.TextField(blank=True)
    post=models.ForeignKey(Post,on_delete=models.CASCADE,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True) 

    class Meta:
       verbose_name='Comment'
    
    def __str__(self):
       return self.comment
    
class Like(models.Model):
   post=models.ForeignKey(Post,on_delete=models.CASCADE,null=True)
   user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

   class Meta:
      unique_together=["post","user"]

   def __str__(self) -> str:
      return f"{self.user} liked on {self.post}"
   
class Follow(models.Model):
   following_user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='following_user')
   followed_user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='followed_user')


   class Meta:
      unique_together=['following_user','followed_user']
   
   def __str__(self) -> str:
      return f"{self.following_user} followed {self.followed_user}"
   


@receiver(post_save, sender=Like)
def update_post_like_count(sender, instance, **kwargs):
    post = instance.post
    post.like_count = Like.objects.filter(post=post).count()
    post.save()

@receiver(post_save, sender=Comments)
def update_post_comments_count(sender, instance, **kwargs):
    post = instance.post
    post.comment_count = Comments.objects.filter(post=post).count()
    post.save()


@receiver(post_delete,sender=Like)
def update_post_like_count_on_delete(sender,instance,**kwargs):
   post=instance.post
   post.like_count=Like.objects.filter(post=post).count()
   post.save()

@receiver(post_delete,sender=Comments)
def update_post_comment_count_on_delete(sender,instance,**Kwargs):
   post=instance.post
   post.comment_count=Comments.objects.filter(post=post).count()
   post.save()









