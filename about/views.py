from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about(request):
    name = 'django'
    experience = 'Entry level'
    working = 'Machine Learning'
    about = {'name' : name, 'ex': experience, 'work': working}
    return render(request, 'about/about.html', context = about)