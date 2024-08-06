from django.urls import path
from .views import home, suivi, sendMessage

app_name = "doctor"

urlpatterns = [
    path("", home, name="home"),
    path("suivi", suivi, name="suivi"),
    path("messages", sendMessage, name="sendMessage"),
]
