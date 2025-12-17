from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from .models import TaskModel
from .serializer import TaskSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class TaksView(ViewSet):
    def list(self, request):
        tasks = TaskModel.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(
            serializer.data, status=status.HTTP_200_OK
        )

    def retrieve(self, request, pk=None):
        try:
            task = TaskModel.objects.get(pk=pk)
            serializer = TaskSerializer(task)
            return Response(
                serializer.data, status=status.HTTP_200_OK
            )
        except:
            return Response(
                {"detail": "Task not found."}, status=status.HTTP_404_NOT_FOUND
            )
        
    def create(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    def update(self ,request, pk=None):
        try:
            task = TaskModel.objects.get(pk=pk)
            serializer = TaskSerializer(task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data, status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )
        except TaskModel.DoesNotExist:            
            return Response(
                {"detail": "Account not found."}, status=status.HTTP_404_NOT_FOUND
            )

    def destroy(self, request, pk=None):
        try:
            task = TaskModel.objects.get(pk=pk)
            task.delete()
            return Response(
                status=status.HTTP_204_NO_CONTENT
            )
        except TaskModel.DoesNotExist:
            return Response(
                {"detail": "Account not found."}, status=status.HTTP_404_NOT_FOUND
            )