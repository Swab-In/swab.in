from django.contrib import admin
from swab_vaksin.models import SwabInformation, VaksinInformation, Experience

# Register your models here.
admin.site.register(SwabInformation)
admin.site.register(VaksinInformation)
admin.site.register(Experience)