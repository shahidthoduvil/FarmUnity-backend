from django.db import models
from Account.models import *
# Create your models here.


class Question(models.Model):
    question=models.TextField(blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)


    
    class Meta:
       verbose_name='Question'

    def __str__(self) :
        return self.question
    
    
class Solution(models.Model):
    answer=models.CharField(max_length=200)
    quest=models.ForeignKey(Question,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
 
    class Meta:
       verbose_name='Solution'

    def __str__(self):
        return self.answer
    

class Notification(models.Model):
    message=models.CharField( max_length=200,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    date=models.DateTimeField(auto_now_add=True)

class Messages(models.Model):
    sender=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name='sender_message')
    receiver=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name='reciever_message')
    message=models.TextField(null=True,blank=True)
    thread_name=models.CharField(null=True,blank=True,max_length=200)
    timestamp=models.DateField(auto_now_add=True)


    def __str__(self) -> str:
        return f'{self.sender.username}-{self.thread_name}' if self.sender else f'{self.message}-{self.thread_name}'



class News(models.Model):
    author=models.CharField(max_length=1000,null=True)
    title = models.CharField(max_length=1000,null=True)
    description = models.TextField(null=True)
    url = models.URLField(max_length=1000,null=True)
    url_to_image = models.URLField(max_length=1000,null=True)

    def __str__(self):
        return self.author