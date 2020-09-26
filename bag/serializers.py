from rest_framework import serializers
from .models import Bag, BagContent
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class BagContentSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    class Meta:
        model = BagContent
        fields = ['id', 'owner', 'bag_content', 'discarded']
class BagSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    contents = BagContentSerializer(many=True, read_only=True)
    active_content = BagContentSerializer(read_only=True)

    class Meta:
        model = Bag
        fields = ['id', 'name', 'contents',  'active_content', 'owner', 'counter', 'discarded_count']

class BagCounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bag
        fields = ['counter']