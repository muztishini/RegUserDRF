from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name
   