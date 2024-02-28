from django.db import models
from users.models import User

# Create your models here.

class Company(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    company_name=models.CharField(max_length=200, null=True, blank=True)
    rec_first_name = models.CharField(max_length=100, null=True, blank=True)
    rec_last_name = models.CharField(max_length=100, null=True, blank=True)
    company_contact_number = models.CharField(max_length=15, null=True, blank=True)
    est_date=models.PositiveIntegerField(null=True, blank=True)
    city=models.CharField(max_length=100, null=True, blank=True)
    state=models.CharField(max_length=100, null=True, blank=True)
    company_address=models.CharField(max_length=500, null=True, blank=True)
    company_website = models.URLField(null=True, blank=True)
    current_company_location=models.URLField(null=True, blank=True)
    company_email_id=models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.company_name
    
    