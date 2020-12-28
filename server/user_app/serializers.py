from rest_framework import serializers
from .models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'my_tasks']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, data):
        user = User(email=data['email'], username=data['username'])
        user.set_password(data['password'])
        user.save()
        return user