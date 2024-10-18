from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date  # Import date


from django.db import models

# CarMake model
class CarMake(models.Model):
    name = models.CharField(max_length=100, unique=True)  
    description = models.TextField(blank=True)  
    country = models.CharField(max_length=100, blank=True)  

    founded_year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name  # Returns the car make name when printed or referenced as a string



# CarModel model
class CarModel(models.Model):
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    
    # Choices for car type
    CAR_TYPE_CHOICES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
    ]

    # Relationship to CarMake model (Many-to-One)
    car_make = models.ForeignKey('CarMake', on_delete=models.CASCADE)  # Many-to-one relationship

    dealer_id = models.IntegerField()  # Refers to a dealer created in Cloudant database
    name = models.CharField(max_length=100)  # Car model name
    car_type = models.CharField(
        max_length=20,
        choices=CAR_TYPE_CHOICES,
        default=SEDAN
    )  # Car type with limited choices
    year = models.DateField(
        validators=[MinValueValidator(date(2015, 1, 1)), MaxValueValidator(date(2023, 12, 31))]
    )  # Car model year with validation for range

    # Additional fields (e.g., color)
    color = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.car_type}, {self.year.year})"
