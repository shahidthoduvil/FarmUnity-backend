from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from datetime import datetime, timedelta 
 
# Create your models here.

class AccountManger(BaseUserManager):
    def _create_user(self,email,password,**extra_fields):
       if not email:
            raise ValueError('Your have not provided a valid e-mail address')
       
       email=self.normalize_email(email)
       user=self.model(email=email,**extra_fields)
       user.set_password(password)
       user.save(using=self._db)
       return user
    

    def create_user(self, email=None, password=None, **extra_fields):
      
        return self._create_user(email, password, **extra_fields)
        
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_admin',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)
    




class Category(models.Model):
    Category_name=models.CharField(max_length=250,blank=True,null=True)
    class Meta:
        verbose_name = 'category'

 
    def __str__(self):
        return self.Category_name

        
class Occupation(models.Model):
    Cat = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)    
    titile=models.CharField(max_length=250,blank=True,null=True)

    class Meta:
        verbose_name = 'Occupation'

 
    def __str__(self):
        return self.titile

class User(AbstractBaseUser):
    first_name=models.CharField(max_length=50,blank=True    )
    last_name=models.CharField(max_length=50,blank=True)
    username=models.CharField(max_length=50,blank=True)
    email=models.EmailField(max_length=100,unique=True,blank=True)
    phone_number=models.CharField(max_length=50,blank=True)
    pic=models.ImageField(upload_to="pro_pic/",null=True,blank=True,default="static/img/userprofile.jpg" )
    cover=models.ImageField(upload_to="cover/",null=True,blank=True,default="static/img/userprofile.jpg" )
    Occup=models.ForeignKey(Occupation,on_delete=models.CASCADE, blank=True , null=True)
    cat=models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)



    #required


    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now_add=True)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_available=models.BooleanField(default=False)


    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','first_name','last_name','phone_number']


    objects=AccountManger()


    def __str__(self):
        return self.email
    
    def has_perm(self,pars,obj=None):
        return self.is_admin
    
    def has_module_perms(self,add_label):
        return True
    def get_last_login_day(self):
        return self.last_login.date()

    def get_last_login_time(self):
        return self.last_login.time()
    
    def is_user_online(self):
        # Assuming that if the user was active within the last 5 minutes,
        # we consider them as "online".
        # You can adjust the timedelta according to application's needs.
        now = datetime.now()
        last_active_threshold = now - timedelta(minutes=5)
        return self.is_active and self.last_login >= last_active_threshold



class Address(models.Model):
        user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
        house_name=models.CharField(max_length=250,unique=False,blank=True)
        landmark=models.CharField(max_length=100,blank=True)
        pincode=models.IntegerField(blank=True)
        city=models.CharField(max_length=200,unique=False,blank=True)
        district=models.CharField(max_length=100,unique=False,blank=True)
        state=models.CharField(max_length=200,unique=False,blank=True)
        country=models.CharField(max_length=150,unique=False,blank=True)
        default=models.BooleanField(default=False,blank=True)





        

            