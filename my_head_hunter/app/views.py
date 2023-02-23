from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login

from .models import *
from .forms import *

# Create your views here.

def login_user(request: WSGIRequest) -> HttpResponse:
    form = Login()
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(username=str(form.cleaned_data['username']))
                if check_password(str(form.cleaned_data['password']), user.password):
                    login(request, user)
                    return redirect('/get/vacancies')
                return redirect('/login/')
            except ObjectDoesNotExist:
                return redirect('/login/')
    return render(request, 'login.html', context={'form': form})

def register(request: WSGIRequest) -> HttpResponse:
    form = Register()
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            if str(form.cleaned_data['choice']) == '1':
                user = Worker(auth_user=User.objects.create_user(
                    username=str(form.cleaned_data['username']),
                    password=str(form.cleaned_data['password']),
                ), name=str(form.cleaned_data['name']))
            else:
                user = Employer(auth_user=User.objects.create_user(
                    username=str(form.cleaned_data['username']),
                    password=str(form.cleaned_data['password']),
                ), name=str(form.cleaned_data['name']))
            user.save()
            login(request, user.auth_user)
            return redirect('/get/vacancies')
    return render(request, 'register.html', context={'form': form})

def edit_worker(request: WSGIRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        return render(request, 'error.html', context={'error': '401 Не авторизован.'})
    form = EditWorker()
    if request.method == 'POST':
        form = EditWorker(request.POST)
        if form.is_valid():
            user = Worker(
                auth_user=user,
                name=str(form.cleaned_data['name']),
                description=str(form.cleaned_data['description']),
                contacts=str(form.cleaned_data['contacts'])
            )
            user.save()
            return redirect('/get/vacancies')
    return render(request, 'edit_worker.html', context={'form': form})

def edit_employer(request: WSGIRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        return render(request, 'error.html', context={'error': '401 Не авторизован.'})
    form = EditEmployer()
    if request.method == 'POST':
        form = EditEmployer(request.POST)
        if form.is_valid():
            user = Employer(
                auth_user=user,
                name=str(form.cleaned_data['name']),
                description=str(form.cleaned_data['description']),
                contacts=str(form.cleaned_data['contacts']),
                address=str(form.cleaned_data['address']),
                amount_of_employees=int(form.cleaned_data['address'])
            )
            user.save()
            return redirect('/get/vacancies')
    return render(request, 'edit_employer.html', context={'form': form})

def get_worker(request: WSGIRequest, id: int) -> HttpResponse:
    try:
        worker = Worker.objects.get(id=id)
        return render(request, 'worker.html', context={'worker': worker, 'user': request.user})
    except ObjectDoesNotExist:
        render(request, 'error.html', context={'error': '400 Соискатель не найден.'})

def get_employer(request: WSGIRequest, id: int) -> HttpResponse:
    try:
        employer = Employer.objects.get(id=id)
        return render(request, 'employer.html', context={'employer': employer, 'user': request.user})
    except ObjectDoesNotExist:
        render(request, 'error.html', context={'error': '400 Работодатель не найден.'})

def send_message() -> HttpResponse:
    pass

def get_messages_list() -> HttpResponse:
    pass

def get_vacancy(request: WSGIRequest, id: int) -> HttpResponse:
    try:
        vacancy = Vacancy.objects.get(id=id)
    except ObjectDoesNotExist:
        return render(request, 'error.html', context={'error': '400 Вакансия не найдена.'})
    return render(request, 'vacancy.html', context={'vacancy': vacancy})

def create_vacancy(request: WSGIRequest) -> HttpResponse:
    form = CreateVacancy()
    if not request.user.is_authenticated:
        return render(request, 'error.html', context={'error': '401 Не авторизован.'})
    employer = None
    for i in Employer.objects.all():
        if i.auth_user == request.user:
            employer = i
    if employer == None:
        return render(request, 'error.html', context={'error': '401 Попытка создать вакансию не от лица компании.'})
    if request.method == 'POST':
        form = CreateVacancy(request.POST)
        if form.is_valid():
            vacancy = Vacancy(
                employer=employer,
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                salary=form.cleaned_data['salary'],
                image=form.cleaned_data['image']
            )
            vacancy.save()
            return redirect('/get/employer')
    return render(request, 'create_vacancy.html', context={
        'user': request.user,
        'form': form
    })

def get_vacancies_list(request: WSGIRequest) -> HttpResponse:
    try:
        vacancies = Vacancy.objects.all()
    except ObjectDoesNotExist:
        vacancies = []
    is_auth = request.user.is_authenticated
    return render(request, 'vacancies_list.html', context={
        'vacancies': vacancies, 
        'is_auth': is_auth,
        'user': request.user
    })
