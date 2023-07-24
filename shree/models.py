from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from shree.manager import EmployeeManager

# Create your models here.
class Employee(AbstractBaseUser):
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    type = models.CharField(max_length = 5, choices=(('E','E'),('HOD','HOD'),('CEO','CEO'),('BM','BM')))
    fname = models.CharField(max_length = 32)
    lname = models.CharField(max_length = 32)
    eid = models.CharField(verbose_name=('EID') ,max_length = 16, unique=True)
    role = models.CharField(max_length = 32)
    department = models.CharField(max_length = 255)
    branch = models.CharField(max_length = 255)
    mobile = models.CharField(max_length = 13)
    email = models.CharField(max_length = 32)
    address = models.TextField(max_length=255)
    arating = models.FloatField(default=0)
    ldays = models.SmallIntegerField(default=2)

    objects = EmployeeManager()
    USERNAME_FIELD = 'eid'
    REQUIRED_FIELDS = []
    

    def __str__(self):
        return str(self.eid)
    
    def has_perm(self, perm, obj=None):
        "Does the Employee have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the Employee have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the Employee a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    
class Review(models.Model):
    femp = models.ForeignKey(Employee, on_delete = models.CASCADE, related_name='from_emp')
    temp = models.ForeignKey(Employee, on_delete = models.CASCADE, related_name='to_emp')
    rating = models.PositiveSmallIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.femp)+' '+'to'+' '+str(self.temp)
    

class Leave(models.Model):
    emp = models.ForeignKey(Employee, on_delete = models.CASCADE)
    df = models.DateField()
    dt = models.DateField()
    type = models.CharField(max_length = 16, choices=(('Casual','Casual'),('Sick','Sick'),('Emergency','Emergency'),('Marriage','Marriage'),('Maternity','Maternity')))
    days = models.PositiveSmallIntegerField()
    status = models.CharField(max_length = 16, choices=(('Pending','Pending'),('Approved','Approved'),('Rejected','Rejected')))
    approved = models.BooleanField(default=False)
    hod_approved = models.BooleanField(default=False)
    ceo_approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.emp)


class Contact(models.Model):
    sno = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 32)
    email = models.CharField(max_length = 32)
    content = models.TextField()

    def __str__(self):
        return "Message from " + self.name + ' - ' + self.email
