from django.db import models
from heis.models import Institution, Page
from recommendations.models import Criterion

# Create your models here.

class Tool(models.Model):
    """Model representing automated tools."""
    class Meta:
        ordering = ("name", )

    name = models.CharField(max_length=100)
    description = models.TextField()
    web_address = models.URLField(unique=True) 

    def __str__(self) -> str:
        return self.name

class Failure(models.Model):
    """Model representing individual failures"""

    criterion = models.ForeignKey(Criterion, on_delete=models.CASCADE, blank=True, null=True)
    review_id = models.ForeignKey('ReviewPage', on_delete=models.CASCADE, blank=True, null=True)
    total_failures = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.criterion.title + " " + str(self.total_failures)

class ReviewPage(models.Model):
    """Model representing induvidual page reviews"""

    page_id = models.ForeignKey(Page, verbose_name='Page', on_delete=models.CASCADE, blank=True, null=True)
    review = models.ForeignKey('ReviewAutomated', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return self.page_id.web_address


class ReviewAutomated(models.Model):
    """Model representing automated reviews"""
    class Meta:
        ordering = ("date_reviewed", )
        verbose_name = "Automated Review"
        verbose_name_plural = "Automated Reviews"
    
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, blank=True, null=True)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE, blank=True, null=True) 
    date_reviewed = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)

    def __str__(self) -> str:
        return self.date_reviewed.strftime('%Y-%m-%d') + " " + self.institution.name   
