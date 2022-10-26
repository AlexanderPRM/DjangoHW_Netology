from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=70)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField(max_length=400)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()
