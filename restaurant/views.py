from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Menu, Booking
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, MenuSerializer, BookingSerializer
from .permissions import IsManager


def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})


class UsersView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method != 'POST':
            permission_classes = [IsManager]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = []
        elif self.request.method != 'GET':
            permission_classes = [IsManager]
        
        return [permission() for permission in permission_classes]


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = []


class BookingView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    def get_queryset(self, **kwargs):
        # getting queryset only for the authenticated user
        queryset = Booking.objects.filter(username=self.request.user)
        return queryset

    def get_permissions(self):
        if self.request.method == 'POST':
            permission_classes = [IsAuthenticated]
        elif self.request.method == 'GET':
            permission_classes = [IsAuthenticated]
        
        return [permission() for permission in permission_classes]


    # def get_queryset(self, **kwargs):
    #     if self.request.method == 'GET':
    #         b = User.objects.filter(username=self.request.user.username)
    #         if b.exists():
    #             queryset = Booking.objects.filter(username=b)
    #             return queryset


    # def get_permissions(self):
    #     if self.request.method == 'POST':
    #         permission_classes = []
    #     elif self.request.method == 'GET':
    #         permission_classes = [IsAuthenticated]
        
    #     return [permission() for permission in permission_classes]