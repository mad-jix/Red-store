from django.db import models

# Part 2.1 Product models
class Products(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'live'),(DELETE,'delete'))
    name=models.CharField(max_length=30)
    price =models.FloatField(default=0)
    description=models.TextField(default=0)
    priorty=models.IntegerField(default=0)
# Part 2.2 Product image model
    image=models.ImageField(upload_to='media/')
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)

    def __str__(self) -> str:
        return self.name

