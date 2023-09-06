from rest_framework import serializers
from .models import Cliente, Logins

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class LoginsSerializer(serializers.ModelSerializer):
    logins = serializers.StringRelatedField(many=True)
    class Meta:
        model = Logins
        fields = ['id', 'login', 'senha', 'logins']
