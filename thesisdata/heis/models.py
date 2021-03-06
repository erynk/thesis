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
    class Meta:
        verbose_name_plural = "Cities"
        ordering = ("city",)

    city = models.CharField(max_length=60)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, verbose_name="region")

    def __str__(self) -> str:
        return self.city

class Institution(models.Model):
    """Model representing an institution of higher education."""
    class Meta:
        ordering = ("name", "city")

    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
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
    cs_major = models.BooleanField(default=False, 
                                   verbose_name="Computer Science related major",
                                   help_text=("True if the institution has a Computer "
                                              "Science major or one related or adjacent "
                                              "to Computer Science, such as Computer "
                                              "Engineering, Computer Information "
                                              "Systems, Information Technology, et cetera"))
    dei_statement = models.BooleanField(default=False,
                                        verbose_name="Diversity and Inclusion Statement",
                                        help_text=("True if the institution "
                                                   "includes accessibility in its "
                                                   "Diversity, Equity, and Inclusion "
                                                   "(or similar) Statement"))
    access_statement = models.BooleanField(default=False,
                                           verbose_name="Accessibility Statement",
                                           help_text=("True if the institution "
                                                      "has a published Accessibility "
                                                      "Statement"))

    def __str__(self) -> str:
        return self.name

class Page(models.Model):
    """Model representing a web page."""
    title = models.CharField(max_length=60, null=True, blank=True)
    web_address = models.URLField(unique=True)
    home_page = models.BooleanField(default=False)
    institution = models.ForeignKey(Institution,  on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.web_address
