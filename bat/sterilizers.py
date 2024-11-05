from rest_framework import serializers
from .models import user_model

class user_model_serializers(serializers.ModelSerializer):
    class Meta:
        model = user_model
        fields = ['id','name', 'email']