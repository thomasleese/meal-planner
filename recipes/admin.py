from django.contrib import admin


from .models import Author, Ingredient, Instruction, Recipe


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = 'name', 'colour', 'website'


class IngredientInline(admin.TabularInline):
    model = Ingredient


class InstructionInline(admin.TabularInline):
    model = Instruction


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = 'name', 'author', 'food', 'serving'
    inlines = IngredientInline, InstructionInline
