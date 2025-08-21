from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    class Roles(models.TextChoices):
        MANAGER = 'MANAGER','Manager'
        OWNER = 'OWNER','Owner'
        TENANT = 'TENANT','Tenant'
    role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.OWNER)

    def __str__(self):
        return f"{self.username} ({self.role})"
    
class PG(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='owner_pgs')

    def __str__(self):
        return self.name
    
class Room(models.Model):
    pg = models.ForeignKey(PG,on_delete=models.CASCADE, related_name='rooms')
    name = models.CharField(max_length=20)
    capacity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name
    
class Bed(models.Model):
    room = models.ForeignKey(Room,on_delete=models.CASCADE, related_name='beds')
    bed_number = models.CharField(max_length=10)
    rent = models.DecimalField(max_digits=10,decimal_places=2)
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.room.name} - bed {self.bed_number}"

class Tenant_Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='tenant_profile')
    pg =   models.ForeignKey(PG,on_delete=models.CASCADE,related_name='tenants')
    room = models.ForeignKey(Room,on_delete=models.CASCADE,related_name='tenants')
    bed =  models.OneToOneField(Bed,on_delete=models.SET_NULL,null=True,blank=True,related_name='tenant')

    join_date = models.DateField(auto_now_add=True)
    deposit = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user.username}->{self.pg.name} / Room {self.room.name} / Bed {self.bed.bed_number}"
