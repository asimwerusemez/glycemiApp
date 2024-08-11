from django.urls import path
from .views import home, suivi, suivi_patient, MessageSendPatientsAndAllMessages, MessageSendDoctor

app_name = "doctor"

urlpatterns = [
    path("", home, name="home"),
    path("suivi/", suivi, name="suivi"),
    path("allPatientsMessages/", MessageSendPatientsAndAllMessages, name="allPatientsMessages"),
    path("suivi_patient/<int:id>/", suivi_patient, name="suivi_patient"),
    path("MessageSendPatients/<int:id>/", MessageSendPatientsAndAllMessages, name="MessageSendPatients"),
    path("MessageSendDoctor/<int:id>/", MessageSendDoctor, name="MessageSendDoctor"),
]

