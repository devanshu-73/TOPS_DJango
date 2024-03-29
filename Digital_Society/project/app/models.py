from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True,max_length=35)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=20)  #chairman / societymember
    isActive = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
class Chairman(models.Model):
    userid = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length = 20)
    lastname = models.CharField(max_length=20)
    contact = models.CharField(max_length=11)
    blockno = models.CharField(max_length=3)
    houseno = models.CharField(max_length=4)
    pic = models.FileField(upload_to="media/upload",default="default.png")

    def __str__(self):
        return self.firstname
class Member(models.Model):
    userid = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length = 20)
    lastname = models.CharField(max_length=20)
    contact = models.CharField(max_length=11)
    blockno = models.CharField(max_length=3)
    houseno = models.CharField(max_length=4)
    occupation = models.CharField(max_length=20)
    job_address = models.TextField()
    bloodgroup = models.CharField(max_length=3)
    vehical_details = models.CharField(max_length=20)
    pic = models.FileField(upload_to="media/upload",default="default.png")

    def __str__(self):
        return self.firstname

class Notice(models.Model):
    authority=models.CharField(max_length=20)
    notice_title = models.CharField(max_length=50)
    notice_text = models.TextField()
    name=models.CharField(max_length=20)
    designation=models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
class Student(models.Model):
    firstname = models.CharField(max_length = 20)
    lastname = models.CharField(max_length=20)
    
    