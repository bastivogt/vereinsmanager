from django.db import models

from django.contrib import admin

from datetime import datetime

import math
# Create your models here.


# Module
class Module(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name



# Position
class Position(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

# Gender
class Gender(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    

# Licennse
class License(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    
# Rate
class Rate(models.Model):
    name = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return f"{self.name}: {self.price}"



class Member(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    birthday = models.DateField()
    gender = models.ForeignKey(Gender, null=True, blank=True, on_delete=models.SET_NULL)
    adress = models.TextField()
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=100, blank=True)
    entry_date = models.DateField()
    account_details = models.TextField(blank=True)

    legal_representative = models.TextField(null=True, blank=True)

    positions = models.ManyToManyField(Position, blank=True)
    modules = models.ManyToManyField(Module, blank=True)
    licenses = models.ManyToManyField(License, blank=True)
    rate = models.ForeignKey(Rate, null=True, blank=True, on_delete=models.SET_NULL)

    chronic_diseases = models.TextField(null=True, blank=True)
    permanent_medication = models.TextField(null=True, blank=True)

    publish_fotos = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)



    #adult_with_child_rate = models.BooleanField(default=False)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.adult_with_child_rate = self.get_adult_with_child_rate()



    @admin.display(description="Fullname")
    def get_fullname(self):
        return f"{self.firstname} {self.lastname}"
    
    @admin.display(description="Age")
    def get_age(self):
        now = datetime.now()
        b_day = datetime.strptime(str(self.birthday), "%Y-%m-%d")
        delta = now - b_day
        return math.floor(delta.days / 365)

    


    

    @admin.display(description="Modules")
    def get_modules_str(self):
        modules = self.modules.all().order_by("name")
        modules_list = [module.name for module in modules]
        return ", ".join(modules_list)
    

    @admin.display(description="Positions")
    def get_positions_str(self):
        positions = self.positions.all().order_by("name")
        positions_list = [position.name for position in positions]
        return ", ".join(positions_list)
    
    @admin.display(description="Licenses")
    def get_licenses_str(self):
        licenses = self.licenses.all().order_by("name")
        licenses_list = [license.name for license in licenses]
        return ", ".join(licenses_list)
    


    def get_adult_with_child_rate(self):
        if self.rate.name == "Kind" and self.get_age() >= 18:
            return True
        return False
    

    def __str__(self):
        return f"{self.get_fullname()}"

    
