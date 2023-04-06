from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Event
from .serializer import EventSerializer  
# Create your views here.
@api_view(['GET'])
def allEvent(request):
    event = Event.objects.all()
    serializer = EventSerializer(event, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getEvent(request):
    event = Event.objects.get("id")
    serializer = EventSerializer(event, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postEvent(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)