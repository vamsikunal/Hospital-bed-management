from django.contrib import admin
from .models import User, Hospital, Bed, PB
# Register your models here.

admin.site.register(User)
admin.site.register(Hospital)
admin.site.register(Bed)
admin.site.register(PB)
