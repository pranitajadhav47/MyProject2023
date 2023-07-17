from django.db import models
from django.contrib.auth.models import User
# Create your models here
class blogcontain(models.Model):
    title =  models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    #author = models.CharField(max_length=100)
    author=models.ForeignKey(User,on_delete=models.CASCADE,default=User.objects.get(username="pranita").pk)
    no_of_line=models.IntegerField()
    img = models.ImageField(upload_to='images/', default='default_product.png')


    def __str__(self):
        return self.title
