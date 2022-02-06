from math import degrees
from turtle import title
from django.db import models

# Create your models here.

class Region(models.Model):
    """Model representing the geographical region of Colorado"""
    region_name = models.CharField(max_length=60)
    
    def __str__(self) -> str:
        return self.region_name

class City(models.Model):
    """
    Model representing the city of the institution.
    In cases where the institution has more than one campus, 
    this entry should default to the city of the institution's
    mailing address.
    """
    city = models.CharField(max_length=60)

    def __str__(self) -> str:
        return self.city

class Institution(models.Model):
    """Model representing an institution of higher education."""
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    public = models.BooleanField(default=True)
    non_profit = models.BooleanField(default=True, verbose_name="Non-profit")
    university = models.BooleanField(default=True, 
                        help_text=("An institution is considered a university "
                                   "if it offers several undergraduate and "
                                   "graduate programs."))
    community_college = models.BooleanField(default=False, 
                                help_text=("True if the institution belongs "
                                           "to the Colorado Community College "
                                           "System (CCCS) or has Community "
                                           "College in its name."))
    votech = models.BooleanField(default=False, 
                                 verbose_name=("Technical or Vocational "
                                               "College or Institution"))

    def __str__(self) -> str:
        return self.name

class Page(models.Model):
    """Model representing a web page."""
    title = models.CharField(max_length=60)
    web_address = models.URLField(unique=True)
    home_page = models.BooleanField(default=False)
    institution = models.ForeignKey(Institution,  on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.web_address
