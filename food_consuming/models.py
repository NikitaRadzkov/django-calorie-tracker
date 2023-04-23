from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Food(BaseModel):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    carbs = models.FloatField()
    proteins = models.FloatField()
    fats = models.FloatField()
    calories = models.IntegerField()


class Consume(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)
