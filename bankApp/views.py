from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveUpdateDestroyAPIView
from .models import SendMoney,LoanRequest
from .serializers import SendMoneySerializer,LoanRequestSerializer,LoanRequestListSerializer,LoanRequestDetailSerializer,UserLoanRequestDetailSerializer,UserLoanRequestUpdateSerializer
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsManager

class SendMoneyView(CreateAPIView):
    queryset = SendMoney.objects.all()
    serializer_class = SendMoneySerializer
    permission_classes = [IsAuthenticated]

class LoanRequestView(CreateAPIView):
    queryset = LoanRequest.objects.all()
    serializer_class = LoanRequestSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LoanRequestListView(ListAPIView):
    queryset = LoanRequest.objects.all()
    serializer_class = LoanRequestListSerializer
    permission_classes = [IsManager]

class LoanRequestDetailView(RetrieveUpdateDestroyAPIView):
    queryset = LoanRequest.objects.all()
    serializer_class = LoanRequestDetailSerializer
    permission_classes = [IsManager]

class UserLoanRequestDetailView(ListAPIView):
    # queryset = LoanRequest.objects.all()
    serializer_class = UserLoanRequestDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return LoanRequest.objects.filter(user=self.request.user)

class UserLoanRequestUpdateView(RetrieveUpdateDestroyAPIView):
    # queryset = LoanRequest.objects.all()
    serializer_class = UserLoanRequestUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return LoanRequest.objects.filter(user=self.request.user)


# class LoanApprovalView(RetrieveUpdateAPIView):
#     queryset = LoanRequest.objects.all()
#     serializer_class = LoanRequestSerializer
#     permission_classes = [IsManager]

#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         is_approved = request.data.get('is_approved', None)

#         if is_approved is not None and isinstance(is_approved, bool):
#             instance.is_approved = is_approved
#             instance.save()
#             return Response({'message': 'Loan request updated successfully'}, status=status.HTTP_200_OK)
#         else:
#             return Response({'message': 'Invalid request. You must specify "is_approved" as a boolean value.'}, status=status.HTTP_400_BAD_REQUEST)

# class LoanRequestListView(ListAPIView):
#     queryset = LoanRequest.objects.all()
#     serializer_class = LoanRequestSerializer
#     permission_classes = [IsManager]

# class AcceptedLoanListView(ListAPIView):
#     serializer_class = AcceptedLoanSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         # Return only accepted loans for the current user
#         return AcceptedLoan.objects.filter(loan_request__user=self.request.user)