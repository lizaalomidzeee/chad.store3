from django.db import models
from config.model_utils.models import TimeStampedModel # type: ignore
 
 
class Category(TimeStampedModel, models.Model):
    name = models.CharField(max_length=255, unique=True)
    products = models.ManyToManyField('products.Product', related_name='categories')
    
    
class CategoryImage(TimeStampedModel, models.Model):
    image = models.ImageField(upload_to='categories/')
    product = models.ForeignKey('categories.Category', related_name='images', on_delete=models.CASCADE)