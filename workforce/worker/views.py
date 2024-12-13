from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Worker
from .serializers import WorkerSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class WorkerList(APIView):
    
    @swagger_auto_schema(
        operation_description="Retrieve a list of all workers",
        responses={
            200: WorkerSerializer(many=True),  
        }
    )
    def get(self, request):
        workers = Worker.objects.all()
        serializer = WorkerSerializer(workers, many=True)
        return Response(serializer.data)

    
    @swagger_auto_schema(
        operation_description="Create a new worker",
        request_body=WorkerSerializer,  
        responses={
            201: WorkerSerializer,  
            400: "Bad Request",  
        }
    )
    def post(self, request):
        serializer = WorkerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WorkerDetail(APIView):
    
    @swagger_auto_schema(
        operation_description="Retrieve details of a specific worker",
        responses={
            200: WorkerSerializer,  
            404: "Worker not found",  
        }
    )
    def get(self, request, pk):
        worker = self.get_object(pk)
        if worker is None:
            return Response({"error": "Worker not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = WorkerSerializer(worker)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Update details of a specific worker",
        request_body=WorkerSerializer,  
        responses={
            200: WorkerSerializer,  
            404: "Worker not found",  
            400: "Bad Request",  
        }
    )
    def put(self, request, pk):
        worker = self.get_object(pk)
        if worker is None:
            return Response({"error": "Worker not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = WorkerSerializer(worker, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    @swagger_auto_schema(
        operation_description="Delete a specific worker",
        responses={
            204: "No Content",  
            404: "Worker not found",  
        }
    )
    def delete(self, request, pk):
        worker = self.get_object(pk)
        if worker is None:
            return Response({"error": "Worker not found"}, status=status.HTTP_404_NOT_FOUND)
        worker.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    def get_object(self, pk):
        try:
            return Worker.objects.get(pk=pk)
        except Worker.DoesNotExist:
            return None

