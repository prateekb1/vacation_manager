from django.db import models
from django.core.exceptions import ValidationError

class Vacation(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    
    def __str__(self):
        return self.name