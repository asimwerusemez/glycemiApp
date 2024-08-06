from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import ConnexionForm, CreateUserDoctorForm, CreateUserPatientForm

def register_doctor(request):
    form = CreateUserDoctorForm()
    if request.method == "POST":
        form = CreateUserDoctorForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts:login')
        else:
            form = CreateUserDoctorForm()
    return render(request, "accounts/register_doctor.html", {"form":form})

def register_patient(request):
    form = CreateUserPatientForm()
    if request.method == "POST":
        form = CreateUserPatientForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts:login')
        else:
            form = CreateUserPatientForm(request.POST, request.FILES)
    return render(request, "accounts/register_patient.html", {"form":form})



def login_user(request):
    form = ConnexionForm(request.POST)
    if request.method == "POST":
        form = ConnexionForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.isDoctor:
                    return redirect('doctor:home')
                if user.isPatient:
                    return redirect('patient:home')
        else:
            form = ConnexionForm()
    return render(request, "accounts/login.html", {"form":form})

def logout_user(request):
    logout(request)
    return redirect('accounts:login')