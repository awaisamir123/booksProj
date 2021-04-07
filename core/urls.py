from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from core import views

# from .views import BookList, BookDetail

urlpatterns = [
    # path('', BookList.as_view()),
    # path('<int:pk>', BookDetail.as_view()),

    # path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
