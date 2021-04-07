from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here

from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/books/', views.HelloView.as_view(), name='books'),
    path('api/v1/books/<int:pk>/', views.BookDetail.as_view()),

    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

]