from django.db import models
from Account.models import User,Category

# Create your models here.


class Banner(models.Model):
    title=models.CharField(max_length=200,blank=True,null=True)
    img=models.ImageField(default='default.jpg', upload_to='Banner')
    is_list=models.BooleanField(default=False)

    class Meta:
        verbose_name='Banner'
    def __str__(self):
        return self.title

        


class Quote(models.Model):
    content=models.TextField(blank=True)
    Author=models.CharField(max_length=20,null=True,blank=True)
    is_list=models.BooleanField(default=False)
    

    class Meta:
       verbose_name="Quote"
    
    def __str__(self):
       return self.Author

class Member(models.Model):
    title=models.CharField( max_length=200,blank=True,null=True)
    img=models.ImageField(default='default.jpg',upload_to='Member')
    is_list=models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
       verbose_name='Member'

    def __str__(self):
       return self.title
    
    def unlist_associated_users(self):
        if self.category:
            associated_users = User.objects.filter(cat=self.category, is_active=True)
            for user in associated_users:
                user.is_active = False
                user.save()
    


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')  
    message = models.TextField()
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    user1 = models.ForeignKey(User, on_delete=models.CASCADE,null=True, related_name='additional_reviews') 

    def __str__(self) :
        return self.message
    
    