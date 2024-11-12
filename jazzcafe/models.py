from django.db import models

# Create your models here.
class Drink(models.Model):
    name = models.CharField(max_length=100)
    yen = models.IntegerField()
    is_out_of_order = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Treat(models.Model):
    name = models.CharField(max_length=100)
    yen = models.IntegerField()
    is_out_of_order = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Order(models.Model):
    register_datetime = models.DateTimeField()
    table_number = models.IntegerField()
    drink = models.ForeignKey(Drink, on_delete=models.PROTECT, null=True, blank=True)
    is_suger = models.BooleanField(default=False)
    is_milk = models.BooleanField(default=False)
    treat = models.ForeignKey(Treat, on_delete=models.PROTECT, null=True, blank=True)
    is_served = models.BooleanField(default=False, null=False)