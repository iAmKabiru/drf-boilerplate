from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserSerializer
from django.views.generic import ListView

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
