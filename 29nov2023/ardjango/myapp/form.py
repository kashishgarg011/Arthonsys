from django import forms
from .models import register_model
gender_choice=[
    ('male','male'),('female','female')
]
city_choice=[
        ('Jaipur','Jaipur'),('dholpur','dholpur'),('udaipur','udaipur'),('ajmer','ajmer')
]
skill_choice=[
        ('python','python'),('c','c'),('java','java'),('oops','oops')
]
class register_form(forms.ModelForm):
    gender=forms.ChoiceField(choices=gender_choice)
    city = forms.ChoiceField(choices=city_choice)
    skill = forms.MultipleChoiceField(choices=skill_choice)

    class Meta:
        model=register_model
        fields=['user_name','email','password','gender','city','skill']