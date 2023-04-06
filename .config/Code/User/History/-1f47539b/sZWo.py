
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Event
from .serializer import EventSerializer  

# Create your views here.
class event_list(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        event = Event.objects.all()
        serializer = EventSerializer(event, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class event_detail(APIView):
    def get(self, request, id=None):
        event = Event.objects.filter(id=id)
        serializer = EventSerializer(event, many=True)
        return Response(serializer.data)
  
    def put(self, request, id=None):
        event = Event.objects.get(id=id)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id=None):
        event = Event.objects.get(id=id)
        serializer = EventSerializer(event, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST, )
    def delete(self, request, id=None):
        event = Event.objects.get(id=id)
        event.delete()
        return Response(status=status.HTTP_202_ACCEPTED )