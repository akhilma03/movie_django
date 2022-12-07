from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=200)
    desc= models.TextField()
    year=models.IntegerField()
    images=models.ImageField(upload_to="gallery",null=True,blank=True)
    
    
    def __str__(self):
        return self.name