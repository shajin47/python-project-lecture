from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Products
from .serializers import productSerializer
# Create your views here.

@api_view(['POST'])
def createProducts(request):
    try:
        data = request.data
        product = Products.objects.create(
            Product_Name = data['Product_Name'],
            HSN_Code = data['HSN_Code'],
            Cost_Price = data['Cost_Price'],
            Selling_Price = data['Selling_Price']
        )
        instance = productSerializer(product)
        return Response(instance.data)
    except:
        return Response({"success": False, "message": "Something went wrong might be duplicate record"})

 


