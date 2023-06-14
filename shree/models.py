from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    type = models.CharField(max_length = 5)
    is_staff = models.BooleanField(default=False)
    first_name = models.CharField(max_length = 32)
    last_name = models.CharField(max_length = 32)
    employee_id = models.CharField(max_length = 16)
    role = models.CharField(max_length = 32)
    department = models.CharField(max_length = 255)
    branch = models.CharField(max_length = 255)
    mobile = models.CharField(max_length = 13)
    email = models.CharField(max_length = 32)
    username = models.CharField(max_length = 32,unique=True)
    password = models.CharField(max_length = 32)
    address = models.TextField(max_length=255)
    arating = models.FloatField(default=0)
    ldays = models.PositiveSmallIntegerField(default=24)
    timeStamp = models.DateTimeField(auto_now_add = True, blank = True)

    USERNAME_FIELD = "username"
    objects = UserManager()

    def __str__(self):
        return str(self.username)

    
class Review(models.Model):
    fuser = models.ForeignKey(User, on_delete = models.CASCADE, related_name='from_user')
    tuser = models.ForeignKey(User, on_delete = models.CASCADE, related_name='to_user')
    rating = models.PositiveSmallIntegerField(default=0)
    timeStamp = models.DateTimeField(auto_now_add = True, blank = True)

    def __str__(self):
        return str(self.fuser)+' '+'to'+' '+str(self.tuser)
    

class Leave(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    df = models.DateField()
    dt = models.DateField()
    type = models.CharField(max_length = 16, choices=(('Casual','Casual'),('Sick','Sick'),('Emergency','Emergency'),('Marriage','Marriage'),('Maternity','Maternity')))
    days = models.PositiveSmallIntegerField(default=24)
    status = models.CharField(max_length = 16, choices=(('Pending','Pending'),('Approved','Approved'),('Rejected','Rejected')))
    approved = models.BooleanField(default=False)
    hod_approved = models.BooleanField(default=False)
    ceo_approved = models.BooleanField(default=False)
    timeStamp = models.DateTimeField(auto_now_add = True, blank = True)
    def __str__(self):
        return str(self.user)


class Contact(models.Model):
    sno = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 32)
    email = models.CharField(max_length = 32)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add = True, blank = True)

    def __str__(self):
        return "Message from " + self.name + ' - ' + self.email
