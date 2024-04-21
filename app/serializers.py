from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile  # Import the Profile model

class CaseInsensitiveChoiceField(serializers.ChoiceField):
    def to_internal_value(self, data):
        data = data.lower()
        return super().to_internal_value(data)

class CreateSerializers(serializers.Serializer):
    
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    profession = CaseInsensitiveChoiceField(choices=(("civilian", "Civilian"), ("lawyer", "Lawyer")))
    password = serializers.CharField(max_length=100)
    
    def validate(self, data):
        if 'name' in data:
            if User.objects.filter(username=data['name']).exists():
                raise serializers.ValidationError("Name already exists.")
        return data
    
    def create(self, validated_data):
        # Create the user
        user = User.objects.create_user(username=validated_data["name"], password=validated_data['password'])
        user.age = validated_data['age']
        user.profession = validated_data['profession']
        user.save()
        
        # Create the corresponding profile
        profile = Profile.objects.create(user=user, age=validated_data['age'], profession=validated_data['profession'])
        
        # Return the validated data
        return validated_data

class LoginSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField(required=False)
    profession = CaseInsensitiveChoiceField(choices=(("civilian", "Civilian"), ("lawyer", "Lawyer")))
    password = serializers.CharField(max_length=100)
    
    def validate(self, data):
        # Validate the name and password fields
        if 'name' not in data:
            raise serializers.ValidationError("Name is required.")
        if 'password' not in data:
            raise serializers.ValidationError("Password is required.")
        
        return data