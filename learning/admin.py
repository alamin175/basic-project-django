from django.contrib import admin
from .models import Learning

# Register your models here.
class LearningAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'email')
admin.site.register(Learning, LearningAdmin)