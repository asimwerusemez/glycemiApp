from django.urls import path
from .views import register_doctor, register_patient, login_user, logout_user

app_name = "accounts"

urlpatterns = [
    path('connexion_patient/', register_patient, name='connexion_patient'),
    path('connexion_doctor/', register_doctor, name='connexion_doctor'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

]
