from django.db import models
from users.models import User

# Create your models here.
 
class Resume(models.Model):
    EXPERIENCE_CHOICES = (
        ('Fresher', 'Fresher'),
        ('Less than 1 year', 'Less than 1 year'),
        ('1-3 years', '1-3 years'),
        ('3-5 years', '3-5 years'),
        ('5-10 years', '5-10 years'),
        ('10+ years', '10+ years'),
    )
    EDUCATION_CHOICES = [
        ('high_school', 'High School'),
        ('associate_degree', 'Associate Degree'),
        ('bachelor_degree', 'Bachelor\'s Degree'),
        ('master_degree', 'Master\'s Degree'),
        ('PhD', 'PhD'),
        ('other', 'Other'),
    ]
    user =models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email=models.EmailField(null=True, blank=True)
    phone_no = models.CharField(max_length=15, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    education = models.CharField(max_length=100, choices=EDUCATION_CHOICES, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    job_title=models.CharField(max_length=100, null=True, blank=True)
    experience = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='Fresher')
    current_position=models.CharField(max_length=100, null=True, blank=True)
    skills = models.TextField(null=True, blank=True)
    upload_resume=models.FileField(upload_to='resume', null=True, blank=True)
    
    # insert cv
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'