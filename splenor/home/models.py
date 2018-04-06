from django.db import models
from django.contrib.auth.models import Permission, User
from multiselectfield import MultiSelectField

# Create your models here.

class Product(models.Model):

    PRODUCT_NAMES = {
        ('Beltbuckle', 'Beltbuckle'),
        ('Button', 'Button'),
        ('Lace', 'Lace'),
        ('Slider', 'Slider'),
        ('Waistbelt', 'Waistbelt'),
        ('Zipper', 'Zipper'),
    }

    product_name = models.CharField(max_length=50, choices=PRODUCT_NAMES)

    def __str__(self):
        return self.product_name

class Zipper(models.Model):

    CATEGORIES = (
        ('Metal', 'Metal'),
        ('Vislon', 'Vislon'),
        ('Nylon', 'Nylon'),
    )

    STYLES = (
        ('Open-end', 'Open-end'),
        ('Close-end', 'Close-end'),
        ('Two-way', 'Two-way'),
        ('Coil', 'Coil'),
        ('Invisible', 'Invisible'),
    )

    type = models.ForeignKey(Product, default=4)
    image = models.FileField(null=True, blank=True)
    desc = models.TextField(blank=True)
    category = models.CharField(max_length=100, choices=CATEGORIES)
    style = MultiSelectField(choices=STYLES, blank=True)

    def __str__(self):
        return self.category

class Slider(models.Model):

    CATEGORIES = (
        ('Metal', 'Metal'),
        ('Plastic', 'Plastic'),
        ('Nylon', 'Nylon'),
        ('Rhinestone', 'Rhinestone'),
    )

    type = models.ForeignKey(Product, default=6)
    image = models.FileField(null=True, blank=True)
    desc = models.TextField(blank=True)
    category = models.CharField(max_length=100, choices=CATEGORIES)

    def __str__(self):
        return self.category


class Waistbelt(models.Model):

    CATEGORIES = (
        ('Genuine Leather', 'Genuine Leather'),
        ('PU Leather', 'PU Leather'),
        ('Silicon Rubber', 'Silicon Rubber'),
        ('Fancy Metal', 'Fancy Metal'),
        ('Elastic', 'Elastic'),
        ('Rhinestone', 'Rhinestone'),
        ('Fabric', 'Fabric'),
        ('Canvas', 'Canvas'),
    )

    type = models.ForeignKey(Product, default=5)
    image = models.FileField(null=True, blank=True)
    desc = models.TextField(blank=True)
    category = models.CharField(max_length=100, choices=CATEGORIES)

    def __str__(self):
        return self.category


class Beltbuckle(models.Model):

    CATEGORIES = (
        ('Pin Buckle', 'Pin Buckle'),
        ('Double Rings', 'Double Rings'),
        ('Alloy', 'Alloy'),                             #alloy
        ('Crystal Metal', 'Crystal Metal'),
        ('Auto', 'Auto'),
    )

    type = models.ForeignKey(Product, default=3)
    image = models.FileField(null=True, blank=True)
    desc = models.TextField(blank=True)
    category = models.CharField(max_length=100, choices=CATEGORIES)

    def __str__(self):
        return self.category


class Lace(models.Model):

    CATEGORIES = (
        ('Cotton', 'Cotton'),
        ('Polyester', 'Polyester'),
        ('Nylon', 'Nylon'),
        ('Elastic', 'Elastic'),
        ('Cotton Fabric', 'Cotton Fabric'),
        ('Woven Embroidery', 'Woven Embroidery'),
        ('Woven Embroidery Fabric', 'Woven Embroidery Fabric'),
        ('Chest', 'Chest'),
        ('Shoulder', 'Shoulder'),
    )

    type = models.ForeignKey(Product, default=1)
    image = models.FileField(null=True, blank=True)
    desc = models.TextField(blank=True)
    category = models.CharField(max_length=100, choices=CATEGORIES)

    def __str__(self):
        return self.category


class Button(models.Model):

    CAREGORIES = (
        ('Metal', 'Metal'),
        ('Plastic', 'Plastic'),
        ('Wooden', 'Wooden'),
        ('Bone Horn', 'Bone Horn'),
        ('Polyester', 'Polyester'),
        ('Shell', 'Shell'),
        ('Cloth', 'Cloth'),
        ('Leather', 'Leather'),
        ('Thread', 'Thread'),
        ('Coconut Shell', 'Coconut Shell'),
        ('Ceramic Garment', 'Ceramic Garment'),
        ('Lace', 'Lace'),
        ('Resin', 'Resin'),
    )

    STYLES = (
        ('Two Hole', 'Two Hole'),
        ('Four Hole', 'Four Hole'),
        ('Press', 'Press'),
        ('Shank', 'Shank'),
        ('Hook and Eye', 'Hook and Eye'),
        ('Coat', 'Coat'),
        ('Shirt', 'Shirt'),
        ('Cardigan', 'Cardigan'),
        ('Toggle', 'Toggle'),
        ('Decorative', 'Decorative'),
    )

    type = models.ForeignKey(Product, default=7)
    image = models.FileField(null=True, blank=True)
    desc = models.TextField(blank=True)
    category = models.CharField(max_length=100, choices=CAREGORIES)
    style = MultiSelectField(choices=STYLES, blank=True)                #multiselectfield

    def __str__(self):
        return self.category

class Teammember(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.name + self.designation

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name + ' - ' + self.email
