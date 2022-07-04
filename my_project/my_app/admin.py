from django.contrib import admin

# Register your models here.
from my_app.models import Customer

# Allows us to see the Customer model in the admin window
admin.site.register(Customer)
