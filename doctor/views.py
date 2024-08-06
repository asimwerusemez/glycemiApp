from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from .forms import MessagesForm
from .models import Messages

User = get_user_model()

@login_required
def home(request):
    all_user_patients = User.objects.filter(isPatient=True)
    all_users = all_user_patients.count()

    all_message = Messages.objects.filter(expediteur__isDoctor=True).count()

    labels = []
    data = []

    for all_user_patient in all_user_patients:
        labels.append(all_user_patient.username)
        data.append(all_user_patient.gycemie.taux_sucre)

    return render(request, "doctor/home.html", {
        "all_users": all_users,
        "labels": labels,
        "data": data,
        "all_message": all_message,
    })

@login_required
def suivi(request):
    users = User.objects.filter(isPatient=True)
    all_message = Messages.objects.filter(expediteur__isDoctor=True).count()
    return render(request, "doctor/suivi.html", {
        "users": users,
        "all_message": all_message,
        })

@login_required
def sendMessage(request, id):
    users = User.objects.filter(isPatient=True)
    all_message = Messages.objects.filter(expediteur__isDoctor=True).count()
    return render(request, "doctor/suivi.html", {
        "users": users,
        "all_message": all_message,
        })

@login_required
def sendMessage(request):
    all_message = Messages.objects.filter(expediteur__isDoctor=True).count()
    messages_recus = Messages.objects.all()
    form = MessagesForm()
    if request.method == "POST":
        form = MessagesForm(request.POST, request.FILES)
        if form.is_valid():
            messages_envoyer = form.save(commit=False)
            messages_envoyer.expediteur = request.user
            messages_envoyer.save()
            return redirect('doctor:sendMessage')
        else:
            form = MessagesForm()
    return render(request, "doctor/messages.html", {
        "messages_recus": messages_recus,
        "form":form,
        "all_message": all_message,
        })

