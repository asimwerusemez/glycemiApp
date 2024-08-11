from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

class Alimentation(models.Model):
    nom = models.CharField(max_length=50)
    vitamine = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nom

class Medicament(models.Model):
    nom = models.CharField(max_length=50)
    dose = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nom

class Messages(models.Model):
    expediteur = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages_envoyer")
    destinateur = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages_recus")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.expediteur.username}: {self.message}"
    
    