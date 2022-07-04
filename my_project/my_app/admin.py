from django.contrib import admin

# Register your models here.
from my_app.models import Customer

admin.site.register(Customer)