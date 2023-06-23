from django.db import models
from django.core.files import File
from PIL import Image
from io import BytesIO

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField()
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('name',)
        
        
    def __str__(self):
        return self.name
    

class Product(models.Model):
    
    UNIT_CHOICES = (
        ('each', 'Each'),
        ('kg', 'kilogram'),
        ('g', 'gram'),
    )
    
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES, default='each')
    slug = models.SlugField()
    description = models.TextField(blank=True, max_length=250, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='media/', blank=True, null=True)
    
    class Meta:
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.name
    
    def get_display_price(self):
        if self.unit == 'each':
            return self.price
        else:
            return f"{self.price} per {self.get_unit_display()}"
    
    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return self.thumbnail.url
            else:
                return 'https://via.placeholders.com/240*240.jpg'
            
    def make_thumbnail(self, image, size= (300, 300)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        
        
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        
        thumbnail = File(thumb_io, name=image.name)
        thumbnail.seek(0)
        
        return thumbnail
    
    def save(self, *args, **kwargs):
        if self.image:
            self.thumbnail = self.make_thumbnail(self.image)
            
        super(Product, self).save(*args, **kwargs)
    
    