from django.urls import path
from profiles_api.views import HelloApi

urlpatterns = [
    path('hello-api/',  HelloApi.as_view(), name='hello api')
]