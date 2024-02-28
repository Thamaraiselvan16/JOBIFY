from django.db import models
from company.models import Company
from users.models import User
# from resume.models import Resume

# Create your models here.

class State(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Industry(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self. name

class Job(models.Model):
    EXPERIENCE_CHOICES = (
        ('Fresher', 'Fresher'),
        ('Less than 1 year', 'Less than 1 year'),
        ('1-3 years', '1-3 years'),
        ('3-5 years', '3-5 years'),
        ('5-10 years', '5-10 years'),
        ('10+ years', '10+ years'),
    )
    
    job_type_choices = (
        ('Remote', 'Remote'),
        ('Onsite', 'Onsite'),
        ('Hybrid', 'Hybrid'),
        ('Full-Time','Full-Time'),
        ('Part-Time','Part-Time'),
        ('Temporary','Temporary'),
        ('Freelance','Freelance'),
        ('Internships','Internships'),
        ('Apprenticeships','Apprenticeships'),
        ('Shift Work','Shift Work'),
        ('Volunteer Work','Volunteer Work'),
        ('Entry-Level','Entry-Level'),
        ('Executive','Executive'),
        ('Commission-Based','Commission-Based'),
        ('Consulting','Consulting'),
        ('Permanent','Permanent'),
    )
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    company=models.ForeignKey(Company, on_delete=models.CASCADE)
    # resume=models.ForeignKey(Resume, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    salary = models.PositiveIntegerField (default=3)
    requirements = models.TextField()
    ideal_candidate = models.TextField()
    is_available = models.BooleanField(default=True)
    timestamp =models.DateTimeField(auto_now_add=True)
    industry = models.ForeignKey(Industry, on_delete=models.DO_NOTHING, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.DO_NOTHING, null=True, blank=True)
    job_type = models.CharField(max_length=20, choices=job_type_choices, null=True, blank=True)
    skills = models.TextField(null=True, blank=True)
    experience = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='Fresher')
    def __str__(self):
        return self.job_title 
    

class ApplyJob(models. Model):
    status_choices = (
        ('Accepted', 'Accepted'),
        ('Declined', 'Declined'),
        ('Pending', 'Pending')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    timestamp= models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=status_choices)
    
    
