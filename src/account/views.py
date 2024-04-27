from rest_framework import generics, response, permissions
from django.http import HttpRequest
from .serializers import RegisterSerializer, UserSerializer 
from .models import User

class RegisterAccAPIView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes=[permissions.AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user_data = UserSerializer(user, context=self.get_serializer_context())
        user = user_data.data
        return response.Response(
            {
                "user": user,
                "message": "User Created Successfully.  Now perform Login to get your token",
            }
        )  


from rest_framework import generics
from .models import User
from .serializers import UserUpdateSerializer


class AccountDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'


class UserListAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer





