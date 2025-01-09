from django.db import models
from django.contrib.auth.models import User as Vendor

BEAN_CHOICES = [
    ('arabica', 'Arabica'),
    ('excelsa', 'Excelsa'),
    ('robusta', 'Robusta'),
    ('liberica', 'Liberica'),]
ROAST_LEVELS = [
    ('light', 'Light'),
    ('medium', 'Medium'),
    ('dark', 'Dark'),]

# Create your models here.
class Coffee(models.Model):
    product_ID = models.AutoField(primary_key=True)
    vendor= models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name="vendor_coffees")
    name = models.CharField(max_length=255)
    origin = models.CharField(max_length=100)
    bean = models.CharField(choices=BEAN_CHOICES)
    taste_profile = models.CharField(max_length=255)
    roast = models.CharField(choices=[('light', 'Light'), ('medium', 'Medium'), ('dark', 'Dark')])
    description = models.TextField()
    # image = models.ImageField(upload_to='coffee_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name