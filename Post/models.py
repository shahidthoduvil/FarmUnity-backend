from django.db import models
from Account.models import User
# Create your models here.

class Post(models.Model):
    image=models.ImageField(upload_to="post_img/",null=True,blank=True)
    title=models.CharField(max_length=100,null=True)
    description=models.TextField(blank=True)
    date=models.DateTimeField(auto_now_add=True)
    like=models.IntegerField(null=True)
    location=models.CharField(max_length=100,null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE,blank=True)

    class Meta:
       verbose_name='Post'

    def __str__(self):
       return self.title


class Comments(models.Model):
    comment=models.TextField(blank=True)
    count=models.IntegerField(null=True)
    post=models.ForeignKey(Post,on_delete=models.CASCADE,blank=True)

    class Meta:
       verbose_name='Comment'

    def __str__(self):
       return self.comment
