from rest_framework import serializers
from router.models import RouterDetails

class RouterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouterDetails
        fields = '__all__'
