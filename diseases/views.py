from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter

from .serializers import DiseaseSerializer
from .models import Disease

# Create your views here.
#Function based views are used here except for getting a list of diseases.
@api_view(['GET'])
def endpointOverview(request):
    
    api_urls = {
        'Create':'/disease-create/',
        'Update':'/disease-update/<str:pk>/',
        'Delete':'/disease-delete/<str:pk>/',
        'Detail View':'/disease-detail/<str:pk>/',
        'List':'/disease-list/',
    }
    return Response(api_urls)
    
#View the details of a paarticular disease.
@api_view(['GET'])
def diseaseDetail(request,pk):
    try:
        diseases_available = Disease.objects.get(id=pk)
        serializer = DiseaseSerializer(diseases_available, many=False)
        return Response(serializer.data)
    except Exception as e:
        return Response(e.args[0],status.HTTP_404_NOT_FOUND)

#Create a new disease.
@api_view(['POST'])
def diseaseCreate(request):
    serializer = DiseaseSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return JsonResponse(serializer.data, safe=False)

#Update the details of of a disease.
@api_view(['POST'])
def diseaseUpdate(request,pk):
    try:
        disease_available = Disease.objects.get(id=pk)
        serializer = DiseaseSerializer(instance=disease_available, data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
    except Exception as e:
        return Response(e.args[0],status.HTTP_404_NOT_FOUND)
    
#Comletely delete a disease.
@api_view(['DELETE'])
def diseaseDelete(request,pk):

    try:
        disease_available = Disease.objects.get(id=pk)
        disease_available.delete()
        return JsonResponse('Deletion was Succesfull')
    except Exception as e:
        return JsonResponse(e.args[0],status.HTTP_404_NOT_FOUND, safe=False)


class DiseaseListView(ListAPIView):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter,)
    search_fields = ('title','symptoms','verified',)