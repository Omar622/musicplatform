from django.db import models

# Create your models here.


class Artist(models.Model):
    stage_name = models.CharField(unique=True, max_length=200)
    social_link = models.CharField(max_length=400, null=False)

    class Meta:
        ordering = ['stage_name']
    
    def __str__(self):
        return self.stage_name
        
