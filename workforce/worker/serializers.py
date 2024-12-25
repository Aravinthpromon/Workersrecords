from rest_framework import serializers
from .models import Worker

class WorkerSerializer(serializers.ModelSerializer):
    
    id = serializers.IntegerField(required=False, help_text="The unique identifier for the worker (auto-generated).")
    name = serializers.CharField(max_length=100, help_text="The full name of the worker.")
    email = serializers.EmailField(help_text="The email address of the worker.")
    role = serializers.CharField(max_length=100, help_text="The job role or title of the worker.")

    class Meta:
        model = Worker
        fields = ['id', 'name', 'email', 'role']

