from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def registration(request):
    if request.method == "POST":
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = UserCreationForm()
    return render(request, 'register/register.html', {'form': fm})

