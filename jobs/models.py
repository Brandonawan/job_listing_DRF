from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ('FT', 'Full-time'),
        ('PT', 'Part-time'),
        ('CT', 'Contract'),
        ('FL', 'Freelance'),
        ('IN', 'Internship'),
    ]

    EXPERIENCE_LEVEL_CHOICES = [
        ('EN', 'Entry Level'),
        ('MI', 'Mid Level'),
        ('SE', 'Senior Level'),
        ('DI', 'Director'),
        ('EX', 'Executive'),
    ]

    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    job_type = models.CharField(max_length=2, choices=JOB_TYPE_CHOICES)
    experience_level = models.CharField(max_length=2, choices=EXPERIENCE_LEVEL_CHOICES)
    salary_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salary_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    posted_date = models.DateTimeField(auto_now_add=True)
    application_deadline = models.DateTimeField(null=True, blank=True)
    company_website = models.URLField(max_length=200, null=True, blank=True)
    contact_email = models.EmailField(max_length=254)
    is_active = models.BooleanField(default=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs')

    def __str__(self):
        return self.title

  