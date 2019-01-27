from django.db import models

# Create your models here.
class Customer(models.Model):
    #location = models.CharField(max_length=200)
    sku = models.IntegerField()

    def _str_(self):
        return '%s' % (self.sku)