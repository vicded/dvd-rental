from django.http import JsonResponse

from .models import Customer
from .serializers import CustomerSerializer


# Create your views here.
def customer_template(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return JsonResponse({'customers': serializer.data})
