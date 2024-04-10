from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    attempts = models.IntegerField(default=6)
    wins = models.IntegerField(default=0)
    loss = models.IntegerField(default=0)
    draw = models.IntegerField(default=0)

    def __str__(self,name):
        return self.name    


