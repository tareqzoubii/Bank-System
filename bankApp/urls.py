from django.urls import path,include
from .views import SendMoneyCreateView

urlpatterns = [
    path('', SendMoneyCreateView.as_view()),
    
]