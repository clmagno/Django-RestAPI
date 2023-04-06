from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Event
from .serializer import EventSerializer  
# Create your views here.
@api_view(['GET'])
def getEvent(request):
    event = event.objects.all()
    serializer = EventSerializer(event, many=True)
    return Response(serializer.data)