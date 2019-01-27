from django.db import models

# Create your models here.
class Customer(models.Model):
    location = models.CharField(max_length=200)

    def _str_(self):
        return '%s' % (self.location)


class Items(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sku = models.IntegerField()