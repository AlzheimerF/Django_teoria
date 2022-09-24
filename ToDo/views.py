from django.shortcuts import render, redirect
from .models import User, ToDo


def registration_view(request):
    info = request.POST
    context = {}
    message = None
    if request.method == "POST":
        name = info.get("Name")
        password = info.get("Password")
        if name and password:
            User.objects.create(name=name, password=password)
            return redirect('create_exercise/')
        else:
            context['message'] = 'Поля не должны быть пустыми!'
    return render(request, 'users_register/registration.html', context=context)

def create_exercise_view(request):
    info = request.POST
    context = {}
    print(info)
    if request.method == "POST":
        name = info.get("Name")
        exercise = info.get("Exercise")
        if name and exercise:
            ToDo.objects.create(name=name, exercise=exercise)
        else:
            context['message'] = 'Поля не должны быть пустыми!'
    all_exercise = ToDo.objects.all()
    context['all_exercise'] = all_exercise
    return render(request, 'users_register/create_exercise.html', context=context)