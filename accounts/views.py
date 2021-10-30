from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserSerializer
from django.views.generic import ListView
from .models import Book
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class BookListView(ListView):
    model = Book
    template_name = 'books_list.html'