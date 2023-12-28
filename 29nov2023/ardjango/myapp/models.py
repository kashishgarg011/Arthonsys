from django.db import models
class register_model(models.Model):
    city_choice=(
        ('Jaipur','Jaipur'),('dholpur','dholpur'),('udaipur','udaipur'),('ajmer','ajmer')
    )
    skill_choice=(
        ('python','python'),('c','c'),('java','java'),('oops','oops')
    )
    user_name=models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    city = models.CharField(choices=city_choice, max_length=100)
    skill = models.CharField(choices=skill_choice, max_length=100)

# Create your models here.
