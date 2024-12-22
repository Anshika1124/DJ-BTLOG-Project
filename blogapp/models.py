from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True, null=True)  
    desc = models.TextField()  
    
    def __str__(self):
        return self.title

	