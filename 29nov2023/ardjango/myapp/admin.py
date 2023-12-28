from django.contrib import admin
from .models import register_model
class registeradmin(admin.ModelAdmin):
    list_display = ['user_name','email','password','gender','city','skill']
admin.site.register(register_model,registeradmin)

# Register your models here.
