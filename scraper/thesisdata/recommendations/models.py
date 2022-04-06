from django.db import models

# Create your models here.

class Principle(models.Model):
    """Model representing a WCAG principle."""
    class Meta:
        ordering = ("principle_id", )

    principle_id = models.IntegerField(verbose_name='ID')
    title = models.CharField(max_length=60, null=True)
    description = models.TextField()

    def __str__(self) -> str:
        return str(self.principle_id) + " " + self.title

class Guideline(models.Model):
    """Model representing a WCAG guideline."""
    class Meta:
        ordering = ("principle", "guideline_id", )
    
    guideline_id = models.IntegerField(verbose_name='ID')
    title = models.CharField(max_length=60, null=True)
    description = models.TextField()
    principle = models.ForeignKey(Principle, on_delete=models.SET_NULL, null=True)
    new21 = models.BooleanField(default=False, verbose_name="New to WCAG 2.1?")

    def __str__(self) -> str:
        return str(self.principle.principle_id) + "." + str(self.guideline_id) + " " + self.title

class Criterion(models.Model):
    """Model representing a WCAG criterion."""
    class Meta:
        verbose_name_plural = "Criteria"
        ordering = ("guideline", "criteria_id", )

    LEVELS_CHOICES= (
        ("1", "A"),
        ("2", "AA"),
        ("3", "AAA"),
    )

    criteria_id = models.IntegerField(verbose_name='ID')
    title = models.CharField(max_length=60, null=True)
    level = models.CharField(max_length=1, choices=LEVELS_CHOICES, null=True)
    description = models.TextField()
    guideline = models.ForeignKey(Guideline, on_delete=models.SET_NULL, null=True)
    new21 = models.BooleanField(default=False, verbose_name="New to WCAG 2.1?")

    def __str__(self) -> str:
        return str(self.guideline.principle.principle_id) + "." + str(self.guideline.guideline_id) + "." + str(self.criteria_id) + " " + self.title