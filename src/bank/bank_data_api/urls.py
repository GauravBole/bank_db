
from django.urls import path
from .views import ListBanks, BankBranchApiView
app_name = "bank_data_api"
urlpatterns = [
    path('banks/', ListBanks.as_view(), name="all_banks"),
    path('', BankBranchApiView.as_view(), name="bank_branch"),
]