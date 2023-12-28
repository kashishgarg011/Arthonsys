from django.http import HttpResponse
from django.shortcuts import render
from .models import register_model
from .form import register_form
def post(request):
    print("kashish")
    if request.method=='POST':
        user_name=request.POST['Username']
        email = request.POST['Email']
        password=request.POST['pssword']
        gender=request.POST['gender']
        city=request.POST['countries']
        skill=request.POST['skill']
        a=register_model(
            user_name=user_name,
            email=email,
            password=password,
            gender=gender,
            city=city,
            skill=skill
        )
        a.save()
        return HttpResponse('You are successfully registered!')
    return render(request,'index.html')

# Create your views here.
def get(request):
    r=register_model.objects.all()
    for i in r:
        return render(request,'showdata.html',{'r':r})
