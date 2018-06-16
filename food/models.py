from django.db import models


class Brand(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=250, unique=True)
    colour = models.CharField(max_length=25, default='black')
    website = models.URLField(blank=True)

    class Meta:
        ordering = 'slug',

    def __str__(self):
        return self.name


class Category(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=250, unique=True)
    colour = models.CharField(max_length=25, default='black')

    class Meta:
        ordering = 'slug',
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Food(models.Model):
    slug = models.SlugField(unique=True)
    singular_name = models.CharField(max_length=250, unique=True)
    plural_name = models.CharField(max_length=250, unique=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='foods'
    )
    tags = models.ManyToManyField('Tag', related_name='foods')

    class Meta:
        ordering = 'slug',

    def __str__(self):
        return self.singular_name


class Nutrition(models.Model):
    pass


class Product(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=250, unique=True)
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, related_name='products'
    )
    gtin = models.CharField(max_length=250, unique=True)

    class Meta:
        ordering = 'slug',

    def __str__(self):
        return self.name


class Serving(models.Model):
    name = models.CharField(max_length=250)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, blank=True, related_name='servings'
    )
    nutrition = models.OneToOneField(
        Nutrition, on_delete=models.CASCADE, related_name='serving'
    )

    def __str__(self):
        return f'{self.name} of {self.product}'


class Tag(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=250, unique=True)

    class Meta:
        ordering = 'slug',

    def __str__(self):
        return self.name
