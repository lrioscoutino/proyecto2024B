from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="users_product",
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=4, default=0.00)
    is_active = models.BooleanField(default=1)

    def __str__(self):
        return self.name

