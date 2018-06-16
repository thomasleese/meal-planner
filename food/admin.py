from django.contrib import admin


from .models import Brand, Category, Food, Nutrition, Product, Serving, Tag


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = 'name', 'colour', 'website'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = 'name', 'colour'


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('singular_name',)}
    list_display = 'singular_name', 'plural_name'


@admin.register(Nutrition)
class NutritionAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = 'name', 'brand', 'gtin'


@admin.register(Serving)
class ServingAdmin(admin.ModelAdmin):
    list_display = 'name', 'product', 'nutrition'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = 'name',
