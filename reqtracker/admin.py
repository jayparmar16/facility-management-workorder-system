from django.contrib import admin
from .models import MainRequest, Item, Completion
from .forms import MainRequestForm
# Register your models here.

admin.site.register(MainRequest)
admin.site.register(Item)
admin.site.register(Completion)
