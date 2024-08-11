from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from doctor.forms import MessagesForm
from .task import update_glycemic_data
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from doctor.models import Alimentation, Medicament, Messages



update_glycemic_data.delay()

User = get_user_model()

@login_required
def home(request):
    user_connected = request.user
    all_user_patients = User.objects.filter(id=user_connected.id)
    all_users = all_user_patients.count()

    alimentations = Alimentation.objects.filter(user=request.user).order_by("nom")[:3]
    medicaments = Medicament.objects.filter(user=request.user).order_by("nom")[:3]

    labels = [
        "taux sucre", "Soif intense",
        "Fatigue extrême",
        "Vision floue","Sécheresse de la bouche",
        "Cicatrisation lente", "Infections fréquentes"
        ]
    data = []

    for all_user_patient in all_user_patients:
        data.append(all_user_patient.gycemie.taux_sucre)
        data.append(all_user_patient.gycemie.soif_intense)
        data.append(all_user_patient.gycemie.fatigue_extreme)
        data.append(all_user_patient.gycemie.vision_flou)
        data.append(all_user_patient.gycemie.secheresse_bouche)
        data.append(all_user_patient.gycemie.cicatrisation_lente)
        data.append(all_user_patient.gycemie.infection_frequente)

    print(data)
    print(labels)

    all_message = Messages.objects.filter(destinateur=request.user).count()

    return render(request, "patients/home.html", {
        "all_users": all_users,
        "labels": labels,
        "data": data,
        "all_message": all_message,

        "alimentations": alimentations,
        "medicaments": medicaments,
    })

from django.db.models import Max

@login_required
def MessageDoctorAndAllMessages(request, id=None):
    user = None
    form = MessagesForm(request.POST or None)
    
    if id:
        user = get_object_or_404(User, id=id)
        if request.method == "POST":
            if form.is_valid():
                new_message = form.save(commit=False)
                new_message.expediteur = request.user
                new_message.destinateur = user
                new_message.save()
                return redirect(reverse("patient:MessageToDoctorAll", args=[id]))
        else:
            form = MessagesForm()
        
        messages_recus = Messages.objects.all()
    else:
        messages_recus = None

    latest_messages = Messages.objects.filter(destinateur__isPatient=True).values('destinateur').annotate(
        latest_message_id=Max('id')
    )
    users_messages = Messages.objects.filter(id__in=[item['latest_message_id'] for item in latest_messages]).order_by("-created_at")

    all_message = Messages.objects.filter(destinateur=request.user).count()

    
    return render(request, "patients/all_messages.html", {
        "form": form,
        "messages_recus": messages_recus,
        "users_messages": users_messages,
        "selected_user": user,

        "all_message": all_message,
    })



def consultation(request):    
    alimentations = Alimentation.objects.filter(user=request.user)
    medicaments = Medicament.objects.filter(user=request.user)

    all_message = Messages.objects.filter(destinateur=request.user).count()


    return render(request, "patients/consult_patient.html", {
        "alimentations": alimentations,
        "medicaments": medicaments,

        "all_message": all_message,
    })