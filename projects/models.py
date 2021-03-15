from django.db import models

# Create your models here.

class Orders(models.Model):
    """Model definition for Orders."""

    name = models.CharField(max_length=30, default='Enter your name')
    phone_no = models.IntegerField()
    email_add = models.CharField(max_length=50, default='abc@gmail.com')
    courier_add = models.TextField(max_length=150, default='1/2, avenue park, new york, us')
    zip_code = models.IntegerField()

    class Meta:
        """Meta definition for Orders."""

        verbose_name = 'Orders'
        verbose_name_plural = 'Orderss'

    def __str__(self):
        """Unicode representation of Orders."""
        return self.name
