from django.db import models

# Create your models here.
class Car(models.Model):
    color = models.CharField(max_length=50, default='white')
    # blank - makes field not required
    # null - means that this field may not have a value
    tyre_type = models.CharField(max_length=10, blank=True, null=True)