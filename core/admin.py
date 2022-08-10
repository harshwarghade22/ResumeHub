from django.contrib import admin
from .models import Academic, Skill,User,Cv,Profile

model_list = [User, Skill,Cv,Academic,Profile]
admin.site.register(model_list)

