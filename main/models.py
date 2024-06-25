from django.db import models

# Create your models here.


class Introduction(models.Model):
    text = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pics/')


class About(models.Model):
    bio = models.TextField()
    skills = models.TextField()
    achievements = models.TextField()


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project_pics/', blank=True, null=True)
    video = models.FileField(
        upload_to='project_videos/', blank=True, null=True)


class Resume(models.Model):
    resume_file = models.FileField(upload_to='resumes/')


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)
