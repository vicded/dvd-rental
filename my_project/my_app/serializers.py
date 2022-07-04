from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    """
    Creates a Serializer class for the Customer model.

    :param
    serializers.ModelSerializer (Class):  Class model for customer.
    """
    class Meta:
        """
        Provides meta data for the Customer serializer.

        :var
        model: Customer model.
        fields: the table fields for the Customer table.
        """
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


