from django.db import models

class GycemieData(models.Model):
    taux_sucre = models.FloatField(default=0.1)
    soif_intense = models.IntegerField(default=0)
    fatigue_extreme = models.IntegerField(default=0)
    vision_flou = models.IntegerField(default=0)
    secheresse_bouche = models.IntegerField(default=0)
    perte_poid = models.IntegerField(default=0)
    cicatrisation_lente = models.IntegerField(default=0)
    infection_frequente = models.IntegerField(default=0)
