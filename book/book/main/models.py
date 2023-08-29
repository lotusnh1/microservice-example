from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title=models.CharField(max_length = 200,unique=True)

    def __str__(self):
        return self.title


class Book(models.Model):
    title=models.CharField(max_length = 200)
    description=models.TextField()
    author=models.JSONField()
    book_img = models.ImageField(upload_to = "images/",blank=True,null=True)
    publisher= models.ForeignKey(User,on_delete=models.PROTECT)

    class Meta:
        unique_together = ('title', 'publisher',)


    def __str__(self):
        return self.title

   
  
