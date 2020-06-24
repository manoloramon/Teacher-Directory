from django.db import models
import django.utils.timezone

# Create your models here.
class Teacher(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    ProfilePicture  = models.ImageField()
    emailAddress  = models.CharField(max_length=255)
    phoneNumber =  models.CharField(max_length=20, null=True)
    roomNumber = models.CharField(max_length=10)
    subjectsTaught =  models.CharField(max_length=255)
    date_created = models.DateTimeField(default=django.utils.timezone.now)
    

    def __str__(self):
        return self.firstName
