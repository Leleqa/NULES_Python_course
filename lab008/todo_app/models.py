from django.db import models

from django.db import models
from django.core.validators import RegexValidator
import uuid

# Create your models here.
numeric_validator = RegexValidator(
    regex=r'^\+380 \(\d{2}\) \d{3}-\d{4}$',
    message="Введіть номер телефону у форматі: +380 (67) 123-4567",
    code='invalid_phone_number'
)



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


    