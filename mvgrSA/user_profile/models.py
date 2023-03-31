from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class user_pofile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    bio=models.TextField()
    dp=models.ImageField()
    mobile=models.IntegerField()
    gender=models.BooleanField()
    def __str__(self):
        return f"{self.user}'s profile"
class user_post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post_name=models.CharField(max_length=100)
    post_file=models.FileField()
    post_likes=models.PositiveIntegerField()
    def __str__(self):
        return f"{self.user}'s post -> {self.post_name}"
    
    