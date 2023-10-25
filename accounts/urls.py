from django.urls import path
from .views import CustomerCreateView

urlpatterns = [
    path('createCustomer/', CustomerCreateView.as_view()),
]