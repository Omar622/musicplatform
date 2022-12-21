from django.db import models
from artists.models import Artist

# Create your models here.
class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default='New Album')
    created = models.DateTimeField(auto_now_add=True)
    released = models.DateTimeField(null=False)
    cost = models.FloatField(null=False)

    def __str__(self):
        return self.name
