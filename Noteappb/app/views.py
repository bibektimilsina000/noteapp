from django.shortcuts import render
from rest_framework import generics
from .models import Note
from .serializers import NoteSerialisers


class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerialisers


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerialisers

# Create your views here.
