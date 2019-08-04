from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Speaker(models.Model):
    name = models.CharField(max_length = 40)
    title = models.CharField(max_length = 50)
    bio = models.TextField(max_length = 1000)
    twitter = models.CharField(max_length = 50, blank = True)
    facebook = models.CharField(max_length = 50, blank = True)
    
    def __str__(self):
        return self.name
    
    
class Track(models.Model):
    title = models.CharField(max_length = 50)
    description = models.TextField(max_length = 1000)
    
    def __str__(self):
        return self.title



SESSION_STATUSES = (
        ('a', 'Approved'),
        ('s', 'Submitted'),
        ('r', 'Rejected'),
    )    
    
class Session(models.Model):
    title = models.CharField(max_length = 50)
    abstract = models.TextField(max_length = 2000)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)
    status = models.CharField(max_length = 1, choices = SESSION_STATUSES)
    
    def __str__(self):
        return self.title
    # Return to the sessions details page. put the exact name below 
    # needs to be the registered name for the details
    def get_absolute_url(self):
        return reverse('sessions_detail', kwargs={'pk':self.pk})