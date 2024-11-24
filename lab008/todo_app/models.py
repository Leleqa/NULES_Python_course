from django.db import models

from django.db import models
from django.core.validators import RegexValidator
import uuid

# Create your models here.
numeric_validator = RegexValidator(r'^\d+$', 'Only numeric values are allowed.')

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Renters(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    FirmName = models.CharField(max_length=50)
    Owner = models.CharField(max_length=50)
    PhoneNum = models.CharField(        
        max_length=20,  
        validators=[numeric_validator],
        help_text="Enter numbers only")
    def __str__(self):
        return self.title


    