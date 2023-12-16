from django.db import models

# Create your models here.
class UserModel(models.Model):
    student_id = models.AutoField(primary_key=True)
    roll = models.IntegerField(default= 0)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    confirm = models.BooleanField()
    registration_no = models.BigIntegerField()
    weight = models.DecimalField(max_digits= 3, decimal_places=2)
    height = models.FloatField()
    Current_time = models.TimeField(null=True, blank=True)
    date_of_birth = models.DateTimeField()
    appointment = models.DateField()
    your_opinion = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=200)
    graduation_date = models.DateTimeField(null=True, blank=True)
    degree = models.CharField(max_length=100, null=True , blank=True)
    photo = models.ImageField(null=False, blank=False)

