import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Worker
from .serializers import WorkerSerializer
from drf_yasg.utils import swagger_auto_schema


logger = logging.getLogger('worker')

def not_found_response(message, pk=None):
    if pk:
        logger.warning(f"{message} ID: {pk}")
    else:
        logger.warning(message)
    return Response({"error": message}, status=status.HTTP_404_NOT_FOUND)

class WorkerList(APIView):

    @swagger_auto_schema(
        operation_description="Retrieve a list of all workers",
        responses={200: WorkerSerializer(many=True),}
    )
    def get(self, request):
        search_term = request.query_params.get('search', None)
        logger.info(f"Query Params Received: {request.query_params}")  
        logger.info(f"Search Term: {search_term}")  
    
        if search_term:
           workers = Worker.objects.filter(name__icontains=search_term)
           logger.info(f"Workers filtered with search term '{search_term}': {workers}")
        else:
           workers = Worker.objects.all()
           logger.info("Retrieved all workers")
    
        serializer = WorkerSerializer(workers, many=True)
        return Response({"status": "success", "data": serializer.data})


    @swagger_auto_schema(
        operation_description="Create a new worker",
        request_body=WorkerSerializer,  
        responses={201: WorkerSerializer, 400: "Bad Request"}
    )
    def post(self, request):
        logger.info(f"Received POST request to create a new worker with data: {request.data}")
        serializer = WorkerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"Worker created with ID: {serializer.data['id']}")
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        logger.error(f"Failed to create worker. Errors: {serializer.errors}")
        return Response({"status": "error", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class WorkerDetail(APIView):

    @swagger_auto_schema(
        operation_description="Retrieve details of a specific worker",
        responses={200: WorkerSerializer, 404: "Worker not found"}
    )
    def get(self, request, pk):
        logger.info(f"Received GET request for WorkerDetail with ID: {pk}")
        worker = self.get_object(pk)
        if worker is None:
            return not_found_response("Worker not found", pk)
        serializer = WorkerSerializer(worker)
        logger.info(f"Worker details retrieved for ID: {pk}")
        return Response({"status": "success", "data": serializer.data})

    @swagger_auto_schema(
        operation_description="Update details of a specific worker",
        request_body=WorkerSerializer,
        responses={200: WorkerSerializer, 404: "Worker not found", 400: "Bad Request"}
    )
    def put(self, request, pk):
        logger.info(f"Received PUT request to update worker with ID: {pk} and data: {request.data}")
        worker = self.get_object(pk)
        if worker is None:
            return not_found_response("Worker not found", pk)
        serializer = WorkerSerializer(worker, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"Worker with ID {pk} updated successfully")
            return Response({"status": "success", "data": serializer.data})
        logger.error(f"Failed to update worker with ID {pk}. Errors: {serializer.errors}")
        return Response({"status": "error", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a specific worker",
        responses={204: "No Content", 404: "Worker not found"}
    )
    def delete(self, request, pk):
        logger.info(f"Received DELETE request for worker with ID: {pk}")
        worker = self.get_object(pk)
        if worker is None:
            return not_found_response("Worker not found", pk)
        worker.delete()
        logger.info(f"Worker with ID {pk} deleted successfully")
        return Response(status=status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(
        operation_description="Partially update details of a specific worker",
        request_body=WorkerSerializer,
        responses={200: WorkerSerializer, 404: "Worker not found", 400: "Bad Request"}
    )
    def patch(self, request, pk):
        logger.info(f"Received PATCH request for partial update of worker with ID: {pk} and data: {request.data}")
        worker = self.get_object(pk)
        if worker is None:
            return not_found_response("Worker not found", pk)
        serializer = WorkerSerializer(worker, data=request.data, partial=True)  
        if serializer.is_valid():
            serializer.save()
            logger.info(f"Worker with ID {pk} partially updated")
            return Response({"status": "success", "data": serializer.data})
        logger.error(f"Failed to partially update worker with ID {pk}. Errors: {serializer.errors}")
        return Response({"status": "error", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return Worker.objects.get(pk=pk)
        except Worker.DoesNotExist:
            return None

