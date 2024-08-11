from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from django.db.models import Sum

from patient.models import GycemieData

from .forms import MessagesForm, AlimentationForm, MedicamentForm
from .models import Messages, Medicament, Alimentation

from django.urls import reverse

User = get_user_model()


from django.db.models import Sum

def pourcentage(request):
    porcent = User.objects.filter(isPatient=True).aggregate(gycemie_sum=Sum("gycemie__taux_sucre"))["gycemie_sum"] or 0
    number = User.objects.filter(isPatient=True).count()

    print(f"la somme de taux du sucre: {porcent} - le nombre des users: {number}")
    
    if number == 0:
        return 0
    
    return "{:.2f}".format((porcent * 100) / number)

from django.db.models import Q

@login_required
def home(request):
    all_user_patients = User.objects.filter(isPatient=True)

    
    all_user_pati = User.objects.filter(
    Q(isPatient=True) & Q(gycemie__taux_sucre__lte=2.5) & Q(gycemie__taux_sucre__gte=1))


    all_users = all_user_patients.count()

    all_message = Messages.objects.filter(expediteur__isDoctor=True).count()

    labels = []
    data = []

    for all_user_patient in all_user_patients:
        labels.append(all_user_patient.username)
        data.append(all_user_patient.gycemie.taux_sucre)

    alimentations = Alimentation.objects.all().order_by("nom")[:3]
    medicaments = Medicament.objects.all().order_by("nom")[:3]

    return render(request, "doctor/home.html", {
        "all_users": all_users,
        "labels": labels,
        "data": data,
        "all_message": all_message,

        "pourcent": pourcentage(request),

        "alimentations": alimentations,
        "medicaments": medicaments,

        "nb_patient_down": all_user_pati.count(),
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
def suivi_patient(request, id):
    user = get_object_or_404(User, id=id)
    alimForm = AlimentationForm(request.POST or None)
    medicForm = MedicamentForm(request.POST or None)
    if request.method == "POST":
        alimForm = AlimentationForm(request.POST or None)
        medicForm = MedicamentForm(request.POST or None)

        if alimForm.is_valid():
            new_alim = alimForm.save(commit=False)
            new_alim.user = user
            new_alim.save()

            return redirect(reverse("doctor:suivi_patient", args=[id]))
        
        if medicForm.is_valid():
            new_medic = medicForm.save(commit=False)
            new_medic.user = user

            new_medic.save()

            return redirect(reverse("doctor:suivi_patient", args=[id]))
        
    else:
        alimForm = AlimentationForm()
        medicForm = MedicamentForm()

    
    alimentations = Alimentation.objects.filter(user=user)
    medicaments = Medicament.objects.filter(user=user)

    all_message = Messages.objects.filter(expediteur=request.user).count()


    return render(request, "doctor/suivi_patient.html", {
        "alimForm": alimForm,
        "medicForm": medicForm,
        "user": user,

        "alimentations": alimentations,
        "medicaments": medicaments,

        "all_message": all_message,
    })


@login_required
def MessageSendDoctor(request, id):
    user = get_object_or_404(User, id=id)
    form = MessagesForm(request.POST or None)
    if request.method == "POST":
        form = MessagesForm(request.POST or None)
        if form.is_valid():
            new_alim = form.save(commit=False)
            new_alim.expediteur = request.user
            new_alim.destinateur = user
            request.user.unread_count += 1
            new_alim.save()
            return redirect(reverse("doctor:MessageSendDoctor", args=[id]))
    else:
        form = MessagesForm()  

    message = Messages.objects.filter(expediteur=request.user, destinateur=user)
    
    return render(request, "doctor/messages.html", {"form": form, "messages_recus": message})


from django.db.models import Max


@login_required
def MessageSendPatientsAndAllMessages(request, id=None):
    user = None
    form = MessagesForm(request.POST or None)
    
    if id:
        user = get_object_or_404(User, id=id)
        if request.method == "POST":
            if form.is_valid():
                new_message = form.save(commit=False)
                new_message.expediteur = request.user
                new_message.destinateur = user
                request.user.unread_count += 1
                new_message.save()
                return redirect(reverse("doctor:MessageSendPatients", args=[id]))
        else:
            form = MessagesForm()
        
        messages_recus = Messages.objects.all()
    else:
        messages_recus = None

    latest_messages = Messages.objects.filter(destinateur__isPatient=True).values('destinateur').annotate(
        latest_message_id=Max('id')
    )
    users_messages = Messages.objects.filter(id__in=[item['latest_message_id'] for item in latest_messages]).order_by("-created_at")

    request.user.unread_count = 0
    request.user.save()
    
    return render(request, "doctor/all_messages.html", {
        "form": form,
        "messages_recus": messages_recus,
        "users_messages": users_messages,
        "selected_user": user,
    })


    





