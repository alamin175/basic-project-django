from django.shortcuts import render
# from .models import Recipe

# Create your views here.
def recipe(request):
    if request.method == 'POST':
        data = request.POST
        receipe_img = request.FILES.get('recipe_img')
        print(receipe_img)
    return render(request, 'recipe/recipe.html')