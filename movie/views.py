from django.shortcuts import render
from rest_framework import filters

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import *
from .serializers import *
import json

import pandas as pd
# Create your views here.

class MovieViewSet(ModelViewSet):
    queryset= Movie.objects.all()
    serializer_class=MovieSerializer


    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['nombre', 'pais']
    

    def get_queryset(self):

        queryset = Movie.objects.all()
        s =  self.request.query_params.get('s') if  ['nombre', 'pais'] else 'nombre' 
        o = self.request.query_params.get('o')
        if o == 'asc':
            queryset = queryset.order_by(s)
        if o == 'desc':
            queryset = queryset.order_by('-'+s)
        return queryset

    @action(detail=False,methods=['GET'])
    def top(self,request):
        queryset= Movie.objects.order_by('calificacion')[:5]
        serializer= MovieSerializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=False,methods=['GET'])
    def summary(self,request):
        df = pd.DataFrame(list(Movie.objects.all().values()))   
        paises=df.value_counts('pais').to_dict()
        calificaciones=df['calificacion'].astype(int).value_counts().to_dict() 

        return Response(json.dumps([paises,calificaciones]))
        
        #return Response(json.dumps({**paises,**calificaciones}))