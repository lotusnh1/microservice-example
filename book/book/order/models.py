from django.db import models
from main.models import Book
from django.contrib.auth.models import User



class Card(models.Model):
    buyer=models.ForeignKey(User,on_delete=models.PROTECT)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    date_order=models.DateTimeField(auto_now=True)
    count=models.TextField()



    def __str__(self):
        return self.buyer.id
