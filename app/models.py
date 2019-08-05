from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.db import models


# Html validation check
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
    
# Check html validation    
def validate_nohtml(value):
    try:
        if value.index('<') > -1:
            raise ValidationError("Html is not allowed")
    except ValueError as e:
        pass
    except Exception as e:
        raise ValidationError(e)


class Session(models.Model):
    title = models.CharField(max_length = 50)
    # Setup validation in the abstract filed
    abstract = models.TextField(max_length = 2000, validators=[validate_nohtml])
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)
    status = models.CharField(max_length = 1, choices = SESSION_STATUSES)
    
    def __str__(self):
        return self.title
    # Return to the sessions details page. put the exact name below 
    # needs to be the registered name for the details
    def get_absolute_url(self):
        return reverse('sessions_detail', kwargs={'pk':self.pk})
