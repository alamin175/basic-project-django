from django.shortcuts import render
from .models import Recipe

# Create your views here.
def recipe(request):
    if request.method == 'POST':
        data = request.POST
        receipe_img = request.FILES.get('recipe_img')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        Recipe.objects.create(
            recipe_img = receipe_img,
            recipe_name = recipe_name,
            recipe_description = recipe_description
        )
        
        print(receipe_img, recipe_name, recipe_description)
    
    queryset = Recipe.objects.all()
    recipes = {'recipes': queryset}
        
    return render(request, 'recipe/recipe.html', context=recipes)