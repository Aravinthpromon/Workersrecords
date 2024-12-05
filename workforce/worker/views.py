from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Worker
from .serializers import WorkerSerializer

class WorkerList(APIView):
    def get(self, request):
        workers = Worker.objects.all()
        serializer = WorkerSerializer(workers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WorkerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WorkerDetail(APIView):
    def get_object(self, pk):
        try:
            return Worker.objects.get(pk=pk)
        except Worker.DoesNotExist:
            return None

    def get(self, request, pk):
        worker = self.get_object(pk)
        if worker is None:
            return Response({"error": "Worker not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = WorkerSerializer(worker)
        return Response(serializer.data)

    def put(self, request, pk):
        worker = self.get_object(pk)
        if worker is None:
            return Response({"error": "Worker not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = WorkerSerializer(worker, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        worker = self.get_object(pk)
        if worker is None:
            return Response({"error": "Worker not found"}, status=status.HTTP_404_NOT_FOUND)
        worker.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
