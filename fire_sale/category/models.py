from django.db import models
from user.models import User

# Category
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=9999, blank=True)

    def __str__(self):
        return self.name


class CategoryFavorite(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category_views = models.IntegerField(default=0)
