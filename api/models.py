from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# USER_TYPE=(1,("RECRUITER"),
# 			2,("STUDENT"))

# class Profile(models.Model):

# 	user = models.OneToOneField(User, on_delete=models.CASCADE)
# 	user_type = models.IntegerField(choices=USER_TYPE, default=1)

class StudentEducation(models.Model):

	name = models.CharField(max_length=100)
	age = models.IntegerField(default=20)
	sslcmarks = models.IntegerField(default=50)
	pumarks = models.IntegerField(max_length=50)
	degree = models.CharField(max_length=100)
	course_name = models.CharField(max_length=100)
	aggregate = models.IntegerField(default=35)
	aboutme = models.TextField()
	skills = ArrayField(ArrayField(models.CharField(max_length=100),null=True),size=500,blank=True,default=list([]))


