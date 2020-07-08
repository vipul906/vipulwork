from .models import User
from django.views import generic
from rest_framework import viewsets
from .serializers import UserSerializers


class IndexView(generic.ListView):
    template_name = 'useractivity/index.html'
    context_object_name = 'user_list'

    def get_queryset(self):
        return User.objects.order_by('-user_name')


class DetailView(generic.DetailView):
    model = User
    template_name = 'useractivity/detail.html'


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-user_name')
    serializer_class = UserSerializers
