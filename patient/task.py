from GlyemiApp.celery import app
from accounts.models import User
from random import choices

from celery import shared_task

# Définition des plages de valeurs possibles
TAUX_SUCRE_CHOICES = [0.1, 0.2 ,1, 1.4, 1.25, 1.26]
SOIF_INTENSE_CHOICES = [0, 1]
FATIGUE_EXTREME_CHOICES = [0, 1]
VISION_FLOU_CHOICES = [0, 1]
SECHERESSE_BOUCHE_CHOICES = [0, 1]
PERTE_POIDS_CHOICES = [0, 1]
CICATRISATION_LENTE_CHOICES = [0, 1]
INFECTION_FRENQUENTE_CHOICES = [0, 1]

@shared_task
def update_glycemic_data():
    users = User.objects.filter(isPatient=True)

    for user in users:
        try:
            user.gycemie.taux_sucre = choices(TAUX_SUCRE_CHOICES)[0]
            user.gycemie.soif_intense = choices(SOIF_INTENSE_CHOICES)[0]
            user.gycemie.fatigue_extreme = choices(FATIGUE_EXTREME_CHOICES)[0]
            user.gycemie.vision_flou = choices(VISION_FLOU_CHOICES)[0]
            user.gycemie.secheresse_bouche = choices(SECHERESSE_BOUCHE_CHOICES)[0]
            user.gycemie.perte_poid = choices(PERTE_POIDS_CHOICES)[0]
            user.gycemie.cicatrisation_lente = choices(CICATRISATION_LENTE_CHOICES)[0]
            user.gycemie.infection_frequente = choices(INFECTION_FRENQUENTE_CHOICES)[0]
            user.gycemie.save()
        except Exception as e:
            # Gestion des erreurs (logging, notification, etc.)
            return f"Erreur lors de la mise à jour de l'utilisateur {user.id}: {e}"

    # Appel récursif pour exécuter la tâche toutes les 3 minutes
    update_glycemic_data.apply_async(countdown=30)


