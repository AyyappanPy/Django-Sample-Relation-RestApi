from django.shortcuts import render
from rest_framework import viewsets
from .serializers import LanguageSerializer, ParadigmSerializer, ProgrammerSerializer
from .models import Language, Paradigm, Programmer

# Create your views here.


class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer


class ProgrmmerView(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer


