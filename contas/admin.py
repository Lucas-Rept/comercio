from django.contrib import admin
from .models import Cliente, Item, Payment

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Item)
admin.site.register(Payment)
