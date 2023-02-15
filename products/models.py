from django.db import models
from autoslug import AutoSlugField
from django.db.models import Sum, Count 

class Category(models.Model):
    title = models.CharField(max_length = 255)
    slug = AutoSlugField(populate_from = 'title', unique = True)

    def __str__(self):
        return self.title

class SubCategory(models.Model):
    title = models.CharField(max_length = 255)
    slug = AutoSlugField(populate_from = 'title', unique = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name = 'sub_categories')
    
    def __str__(self):
        return self.category.title + ' -> ' + self.title

class ProductOption(models.Model):
    title = models.CharField(max_length = 255) 

    def __str__(self):
        return self.title

class ProductOptionValue(models.Model):
    title = models.CharField(max_length = 255)
    product_option = models.ForeignKey(ProductOption, on_delete = models.CASCADE, related_name = "product_option_values")

    def __str__(self):
        return self.product_option.title + ' -> ' + self.title

class ProductParam(models.Model):
    title = models.Charfield(max_length = 255)

    def __str__(self):
        return self.title 

class ProductParamValue(models.Model):
    title = models.CharField(max_length = 255) 
    product_param = models.ForeignKey(ProductParam, on_delete  = models.CASCADE, related_name = "product_params_values") 

    def __str__(self): 
        return self.product_param.title + ' -> ' + self.title 

class Product(models.Model):
    title = models.CharField(max_length = 255) 
    description = models.TextField() 
    price = models.IntegerField(default = 0) 
    params = models.ManyToManyField(ProductParam, related_name = 'product_params') 
    options = models.ManyToManyField(ProductOption, related_name = 'product_options') 
    category = models.ManyToManyField(SubCategory, related_name = 'sub_categories') 

    def __str__(self):
        return self.title 

class ProductImage(models.Model):
    image = models.ImageField(upload_to = 'products/')
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name = 'list_images')

    def __str__(self):
        return self.product.title

