from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=300, null=True)
    price = models.FloatField()
    stock = models.IntegerField()
    available = models.BooleanField(default=True)

    # user = models.ManyToManyField("users.User", related_name="product")
