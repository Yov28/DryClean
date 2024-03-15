from typing import Iterable
from django.db import models
from django.conf import settings

# Create your models here.
class User(models.Model):
  username  = models.CharField(max_length=255, blank= True)
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  email = models.EmailField()
  password = models.CharField(max_length=100, blank=True)

  def __str__(self):
    return f"{self.firstname} {self.lastname}"

class Service(models.Model):
  name = models.CharField(max_length=255)
  category = models.CharField(max_length=255,
                              choices=(
                                  ('everyday', 'Everyday Services'),
                                  ('premierservice', 'Premier Services'),
                                  ('shortening', 'Shortening Services'),
                                  ('zip', 'New Zip Services'),
                                  ('resize', 'Resizing Services'),
                                  ('misc', 'Miscellaneous Services'),
                                  ('household', 'Household Services'),
                                  ('formal', 'Formal Wear Services'),
                                  ('leather/suede', 'Leather/Suede Services'),
                                  ('misc', 'Miscellaneous Services')
                              ))
  tag = models.CharField(max_length=255,
                              choices=(
                                  ('dryclean', 'Everyday Services'),
                                  ('laundry', 'Laundry Services'),
                                  ('tailoring', 'Tailoring Services'),
                                  ('specialist', 'Specialists Services')
                              ))
  price = models.CharField(max_length=255)


class Booking(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  product = models.ForeignKey(Service, on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField(default=1)
  booking_date = models.DateTimeField('Date')
  booking_time = models.TimeField('Time')
  total_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

  def save(self, *args, **kwargs):
    if not self.total_cost:
      self.total_cost = self.quantity * self.product.price
    super().save(*args, **kwargs)

@property
def is_complete(self):
  return self.status in ['paid', 'completed']

BOOKING_STATUS_CHOICES = (
  ('pending', 'Pending'),
  ('paid', 'Paid'),
  ('processing', 'Processing'),
  ('completed', 'Completed'),
)
