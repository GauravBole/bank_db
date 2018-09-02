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

        result_qs = Branch.objects.all()
        serializer = BankBranchSerilizer(result_qs, many=True)
        try:
            ifsc_code = request.GET.get('ifsc_code')
        except:
            ifsc_code = None

        try:
            city = request.GET.get('city')
        except:
            city = None
        try:
            bank_name = request.GET.get('bank')
        except:
            bank_name = None

        try:
            if city is not None:
                result_qs = Branch.objects.filter(city__icontains = city)

            if bank_name is not None:
                result_qs = Branch.objects.filter(bank__bank_name__icontains = bank_name)

            if ifsc_code is not None:
                result_qs = Branch.objects.filter(ifsc__icontains = ifsc_code)

            if city is not None and bank_name is not None:
                result_qs = Branch.objects.filter(Q(bank__bank_name__icontains= bank_name)| Q(city__icontains=city))

            serializer = BankBranchSerilizer(result_qs, many=True)

            return Response(serializer.data)
        except:
            return Response({'result': 'Missing fields'}, status=status.HTTP_400_BAD_REQUEST)


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

    def get_queryset(self):
        longitude = self.request.query_params.get('ifsc_code')
        print(">>>>>>>>>>>>>>>",longitude)

# class BankBranchApiView(ListAPIView):
#     queryset = Branch.objects.all()
#     serializer_class = BankBranchSerilizer
#     filter_backends = [SearchFilter]
#     search_fields = ['city']

