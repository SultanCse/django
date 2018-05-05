from django.db import models 

# Create your models here.
class Products_list(models.Model):
    title = models.CharField(max_length=120)
    price = models.CharField(max_length=120)
    description = models.CharField(max_length=220)
    image = models.FileField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.title + '   ' + self.price + '   ' + self.description + '   ' + str(self.image)
