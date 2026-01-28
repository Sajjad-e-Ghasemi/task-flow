from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from .serializer import AccountSerializer 
from .models import Account

# Create your views here.

class AccountView(ViewSet):
    def list(self, request):
        querysets = Account.objects.all()
        serializer = AccountSerializer(querysets, many=True)
        return Response(
            serializer.data, status=status.HTTP_200_OK
        )
    
    def retrieve(self, request, pk=None):
        try:
            account = Account.objects.get(pk=pk)
            serializer = AccountSerializer(account)
            return Response(
                serializer.data, status=status.HTTP_200_OK
            )
        except Account.DoesNotExist:
            return Response(
                {"detail": "Account not found."}, status=status.HTTP_404_NOT_FOUND
            )
        
    def create(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )
    
    def update(self, request, pk=None):
        try:
            account = Account.objects.get(pk=pk)
            serializer = AccountSerializer(account, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data, status=status.HTTP_200_OK
                )
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        except Account.DoesNotExist:
            return Response(
                {"detail": "Account not found."}, status=status.HTTP_404_NOT_FOUND
            )
        
    def destroy(self, request, pk=None):
        try:
            account = Account.objects.get(pk=pk)
            account.delete()
            return Response(
                status=status.HTTP_204_NO_CONTENT
            )
        except Account.DoesNotExist:
            return Response(
                {"detail": "Account not found."}, status=status.HTTP_404_NOT_FOUND
            )

            