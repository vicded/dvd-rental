from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
                    'customer_id',
                    'store_id',
                    'first_name',
                    'last_name',
                    'email',
                    'address',
                    'activebool',
                    'create_date',
                    'last_update',
                    'active'
        ]


