from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class AccountView(APIView):
    def get(self, request):
        return Response({"message": "Hello, this is the Accounts view!"})