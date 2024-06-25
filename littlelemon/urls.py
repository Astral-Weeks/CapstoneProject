from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from restaurant import views
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'users', views.UsersView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('restaurant.urls')),
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api-token-auth/', obtain_auth_token),
    path('restaurant/booking/', views.BookingView.as_view(), name='book'),
]
