from django.db import models

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Resume(models.Model):
    name = models.CharField(max_length=100)
    resume_file = models.FileField(upload_to="resumes/")