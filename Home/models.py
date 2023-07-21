from django.db import models

# Create your models here.


class Banner(models.Model):
    title=models.CharField(max_length=50,blank=True,null=True)
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
    title=models.CharField( max_length=50,blank=True,null=True)
    img=models.ImageField(default='default.jpg',upload_to='Member')
    is_list=models.BooleanField(default=False)

    class Meta:
       verbose_name='Member'

    def __str__(self):
       return self.title
    

