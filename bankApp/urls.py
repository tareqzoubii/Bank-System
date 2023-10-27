from django.urls import path
from .views import SendMoneyView

urlpatterns = [
    path('send-money/', SendMoneyView.as_view()),
    # path('transactions/', SendMoneyListView.as_view()),
]
