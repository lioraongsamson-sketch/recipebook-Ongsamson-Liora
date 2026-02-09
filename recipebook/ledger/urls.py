from django.urls import path

from .views import index, recipes_list, recipe_1

app_name = 'ledger'

urlpatterns = [
    path('', index, name="index"),
    path('recipes/list/', recipes_list, name="recipes_list"), 
    path('recipe/1', recipe_1, name="recipe_1"), 
]
