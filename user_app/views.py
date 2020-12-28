from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from django.contrib.auth import authenticate, login, logout

class UserList(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, format=None):
        """
        return a list of users
        """
        if request.user.is_authenticated:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
        return Response({"errors": "You must be logged in to view this!"})

    def post(self, request, format=None):
        """
        basically the register method
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # TODO - should register log the user in as well?
            return Response(serializer.data)
        return Response(serializer.errors)

class UserSession(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, format=None):
        """
        return a user if they're logged in
        """
        # return Response(UserSerializer(request.user).data)
        if request.user.is_authenticated:
            return Response(UserSerializer(request.user).data)    
        return Response(UserSerializer(User()).data)

    def post(self, request, format=None):
        """
        basically the login method
        """
        try:
            user_from_db = User.objects.get(email=request.data.get('email', ''))
            user = authenticate(username=user_from_db.username,
                password=request.data.get('password', ''))
            if user == None:
                return Response({"errors": "Invalid login attempt!"})
            login(request, user)
            return Response(UserSerializer(user).data)
        except User.DoesNotExist as error:
            print(error)
        return Response({"errors": "Invalid login attempt!"})

    def delete(self, request, format=None):
        """
        basically the logout method
        """
        logout(request)
        return Response({"message": "goodbye!"})

class UserDetails(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, user_id, format=None):
        """
        TODO - return user matching user_id
        """
        print(f"The user_id is: {user_id}")
        return Response({"message": "TODO"})

    # maybe post could be changing passwords or something

    def put(self, request, user_id, format=None):
        """
        TODO - update user matching user_id
        """
        return Response({"message": "TODO"})

    def delete(self, request, user_id, format=None):
        """
        TODO - delete user matching user_id
        """
        return Response({"message": "TODO"})