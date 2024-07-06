from django.shortcuts import render
from . forms import ShowFormsData

# Create your views here.
def contact(request):
    number = "01586075605"
    name = 'Alamin'
    position = 'web developer'
    money = 500
    details = {'number': number, 'name': name, 'ps':position, 'money':money}
    return render(request, 'contact/contact.html', context=details)

def showForms(request):
    if request.method == 'POST':
        fm = ShowFormsData(request.POST)
        print(fm)
        print('this is post method')
        print(fm.cleaned_data)
    else:
     fm = ShowFormsData()
     print('this is get method')
    return render(request, 'contact/forms.html', {'form': fm} )