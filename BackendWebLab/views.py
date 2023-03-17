from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from BackendWebLab.models import Phone,Phonebrand,Phonetype
from BackendWebLab.serializers import DeviceSerializer
from django.http import HttpResponseRedirect


@api_view(['GET', 'POST'])
def Devicedata(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        device = Phone.objects.all()
        serializer = DeviceSerializer(device, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)