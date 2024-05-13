from django.db import models

from django.contrib import admin

from datetime import datetime

import math
# Create your models here.


class Module(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Gender(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Member(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    birthday = models.DateField()
    gender = models.ForeignKey(Gender, null=True, blank=True, on_delete=models.SET_NULL)
    adress = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    entry_date = models.DateField()
    account_details = models.TextField()

    legal_representative = models.TextField(null=True, blank=True)

    positions = models.ManyToManyField(Position, blank=True)
    modules = models.ManyToManyField(Module, blank=True)

    chronic_diseases = models.TextField(null=True, blank=True)
    permanent_medication = models.TextField(null=True, blank=True)

    publish_fotos = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)



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
    

    def __str__(self):
        return f"{self.get_fullname()}"

    
