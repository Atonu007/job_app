from django.db import models

# Create your models here.
class Uploads(models.Model):
    image = models.ImageField(upload_to='images')
    description = models.CharField(max_length=200)


    def __str__(self) -> str:
        return self.description
    

class UploadFiles(models.Model):
    files = models.FileField(upload_to='files')
    description = models.CharField(max_length=200)


    def __str__(self) -> str:
        return self.description
    
    