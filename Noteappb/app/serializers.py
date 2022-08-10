from rest_framework import serializers
from .models import Note


class NoteSerialisers(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'Title', 'Body')
        model = Note
