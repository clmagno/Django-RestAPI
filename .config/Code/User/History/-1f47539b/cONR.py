from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def getEvent(request):
    event = event.objects.all()
    serializer = FoodSerializer(food, many=True)
    return Response(serializer.data)