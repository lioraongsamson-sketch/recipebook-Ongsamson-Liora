from django.urls import path

from .views import recipes_list, recipe_1, recipe_2, RecipeDetailView, RecipeListView

app_name = 'ledger'

urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name="recipes_list"), 
    ##path('recipe/1', recipe_1, name="recipe_1"),
    ##path('recipe/2', recipe_2, name="recipe_2"),  
    path('<int:pk>', RecipeDetailView.as_view(), name="recipe_detail")
]
