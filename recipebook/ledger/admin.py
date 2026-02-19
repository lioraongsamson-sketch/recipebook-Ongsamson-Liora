from django.contrib import admin

from .models import Recipe, RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe


admin.site.register(Recipe, RecipeAdmin)
# Register your models here.
