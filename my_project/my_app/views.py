from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Customer
from .serializers import CustomerSerializer


# Create your views here.

@api_view(['GET', 'POST'])
def customer_template(request):
    """
    Gets and Posts data from and to the JSON dictionary of Customers model.

    :return: Json response with the Customers data.
    """
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response({'customers': serializer.data})

    if request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT'])
def customer_detail(request, id):
    """
    Gets and Puts a value specified by id into Customers JSON.

    :param request: the http request.
    :param id: int value that represents the primary key for the object
    :return: The value of the object specified by the id
    """
    try:
        customer = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



