from django.db import models
# from datetimeutc.fields import DateTimeUTCField
from django.contrib.auth.models import User

# Create your models here.



# --- PROFILE MODEL
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=50, default='default city')
    image = models.CharField(max_length=1000, default='https://undark.org/wp-content/uploads/2020/02/GettyImages-1199242002-1-scaled.jpg')
    display_name = models.CharField(max_length=100, default='display name')

    def __str__(self):
        return self.display_name
    



#  --- CITY MODEL
class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    image = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']



# --- POST MODEL
class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=5000)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']


# --- COMMENT MODEL
class Comment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField('', max_length=5000)
    created = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.profile

    class Meta:
        ordering = ['-created']





