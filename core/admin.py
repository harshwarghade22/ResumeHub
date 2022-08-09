from django.contrib import admin
from .models import Academic, Skill,User,Cv

model_list = [User, Skill,Cv,Academic]
admin.site.register(model_list)

