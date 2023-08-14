from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Hospital(models.Model):
    hospitalname = models.CharField(max_length=50)
    hospitalcode = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.hospitalcode

class Bed(models.Model):
    hospitalcode = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    bedtype1 = models.IntegerField(null=True)
    bedtype2 = models.IntegerField(null=True)
    bedtype3 = models.IntegerField(null=True)

    def __str__(self):
        return self.hospitalcode.hospitalname

class PB(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hospitalcode = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    bedtype = models.CharField(max_length=50)

    def __str__(self):
        return self.user.name