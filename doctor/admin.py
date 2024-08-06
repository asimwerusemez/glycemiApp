from django.contrib import admin
from .models import Medicament, Alimentation, Messages

# Register your models here.

admin.site.register(Alimentation)
admin.site.register(Medicament)
admin.site.register(Messages)
