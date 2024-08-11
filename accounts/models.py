from django.db import models
from django.contrib.auth.models import AbstractUser

from patient.models import GycemieData

class User(AbstractUser):
    nom = models.CharField(max_length=50)
    profession = models.CharField(max_length=50, blank=True, null=True)
    telephone = models.CharField(max_length=50)
    adresse = models.CharField(max_length=200)
    photo_profile = models.ImageField(upload_to="photos_profile")
    isDoctor = models.BooleanField(default=False)
    isPatient = models.BooleanField(default=False)
    unread_count = models.IntegerField(default=0)
    
    gycemie = models.ForeignKey(GycemieData, on_delete=models.CASCADE, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Votre logique pour enregistrer l'utilisateur ici
        super().save(*args, **kwargs)

        # Enregistrement de la table GycemieData associée
        if not self.gycemie:
            gycemie_data = GycemieData.objects.create(
                taux_sucre=0.1,
                soif_intense=0,
                fatigue_extreme=0,
                vision_flou=0,
                secheresse_bouche=0,
                perte_poid=0,
                cicatrisation_lente=0,
                infection_frequente=0
            )
            self.gycemie = gycemie_data
            super().save(*args, **kwargs)


