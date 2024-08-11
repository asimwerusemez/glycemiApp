from django.urls import path
from .views import home, MessageDoctorAndAllMessages, consultation

app_name = "patient"

urlpatterns = [
    path("", home, name="home"),
    path("MessageDoctorAndAllMessages/", MessageDoctorAndAllMessages, name="MessageToDoctor"),
    path("MessageDoctorAndAllMessages/<int:id>", MessageDoctorAndAllMessages, name="MessageToDoctorAll"),
    path("consultation", consultation, name="consultation"),
]
