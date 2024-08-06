from django.shortcuts import render
from .task import update_glycemic_data
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from doctor.models import Messages


def update_data(request):
    task = update_glycemic_data.delay()

    # Vous pouvez renvoyer une réponse à l'utilisateur, par exemple :
    return render(request, 'patients/update_complete.html', {'task_id': task.id})


User = get_user_model()

@login_required
def home(request):
    user_connected = request.user
    all_user_patients = User.objects.filter(id=user_connected.id)
    all_users = all_user_patients.count()

    all_message = Messages.objects.filter(expediteur__isPatient=True).count()

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

    return render(request, "patients/home.html", {
        "all_users": all_users,
        "labels": labels,
        "data": data,
        "all_message": all_message,
    })

