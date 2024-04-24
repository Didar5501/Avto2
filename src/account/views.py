from rest_framework import generics, response, permissions
from django.http import HttpRequest
from .serializers import RegisterSerializer, UserSerializer 
from .models import User

class RegisterAccApi(generics.GenericAPIView):
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

    # def get(self, request: HttpRequest, *args, **kwargs):  # Отдельно Для лист апи вью
    #     users = User.objects.all()
    #     user_data = UserSerializer(users, many=True)
    #     return response.Response(user_data.data)


from rest_framework import generics
from .models import User
from .serializers import UserUpdateSerializer

class UpdateUserApi(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    lookup_field = 'id'


from rest_framework.generics import DestroyAPIView

class UserDeleteAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class AccountDetailApi(generics.RetrieveUpdateDestroyAPIView): #Использовать для получения данных, редактирования и удаления по ID
    queryset = User.objects.all()
    serializer_class = UserSerializer