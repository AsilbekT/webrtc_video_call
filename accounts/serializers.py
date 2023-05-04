
from rest_framework import serializers
from .models import MobileUser


class MobileUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileUser
        fields = ['id', 'phone_number', 'username', 'first_name',
                  'last_name', 'date_joined', 'avatar', 'is_active']
