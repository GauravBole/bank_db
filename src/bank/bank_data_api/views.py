from django.shortcuts import render
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter,OrderingFilter
from .models import Bank, Branch

from .serializers import BankSerializer, BankBranchSerilizer

class ListBanks(APIView):
    def get(self, request, format=None):
        """
            Return a list of all Banks.
        """
        banks = Bank.objects.all()
        serializer = BankSerializer(banks, many=True)
        return Response(serializer.data)


class BankBranchApiView(APIView):
    def get(self, request, format=None):

        branches = Branch.objects.all()
        serializer = BankBranchSerilizer(branches, many=True)
        return Response(serializer.data)

    def post(self,requset, format=None):
        try:
            ifsc_code = requset.data['ifsc_code']
        except:
            ifsc_code = None
        try:
            city = requset.data['city']
        except:
            city = None
        try:
            bank_name = requset.data['bank']
        except:
            bank_name = None

        try:
            if ifsc_code is not None:
                result_qs = Branch.objects.filter(ifsc__icontains = ifsc_code)
            if city is not None and bank_name is not None:
                result_qs = Branch.objects.filter(Q(bank__bank_name__icontains= bank_name)| Q(city__icontains=city))

            serializer = BankBranchSerilizer(result_qs, many=True)
            return Response(serializer.data)
        except:
            return Response({'result': 'Missing fields'}, status=status.HTTP_400_BAD_REQUEST)



# class BankBranchApiView(ListAPIView):
#     queryset = Branch.objects.all()
#     serializer_class = BankBranchSerilizer
#     filter_backends = [SearchFilter]
#     search_fields = ['city']

