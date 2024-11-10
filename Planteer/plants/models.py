from django.db import models

# Create your models here.
class Plant(models.Model):
    #  inner class uses Django TextChoices to define the choices for category
    class CategoryChoices(models.TextChoices):
        FLOWERS = 'FLOWERS', 'Flowers'
        TREES = 'TREES', 'Trees'
        FRUITS = 'FRUITS', 'Fruits'

    name = models.CharField(max_length = 256)
    is_edible = models.BooleanField(default = False)
    about = models.TextField(default="The tree is essintial to the environement and help produce fresh air")
    used_for = models.TextField()
    image = models.ImageField(upload_to="images/", default = "default.jpg")
    category = models.CharField(max_length=20, choices=CategoryChoices.choices, default=CategoryChoices.TREES,)
