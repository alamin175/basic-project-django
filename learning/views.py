from django.shortcuts import render
from django.http import HttpResponse
from learning.models import Learning

# Create your views here.
def learning(request):
    return render(request, 'learning/learn.html')

def checking(request):
    return render(request, 'learning/check.html')

def db_table(request):
    learn = Learning.objects.all()
    return render(request, 'learning/db_table.html', {'learn':learn})