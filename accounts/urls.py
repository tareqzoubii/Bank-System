from django.urls import path
from .views import CustomerCreateView,CustomerListView,CustomerRetrieveUpdateView

urlpatterns = [
    path('createCustomer/', CustomerCreateView.as_view()),
    path('customers/',CustomerListView.as_view()),
    path('me/',CustomerRetrieveUpdateView.as_view()),
]