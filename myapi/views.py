from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from router.models import RouterDetails
from .seriealizers import RouterSerializer
from rest_framework import status

class RouterView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return RouterDetails.objects.get(pk=pk,status=1)
        except RouterDetails.DoesNotExist:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,pk=None):
        if pk != None:
            router = self.get_object(pk=pk)
            result = RouterSerializer(router)
        else:
            router = RouterDetails.objects.all().filter(status=1)
            result = RouterSerializer(router,many=True)       
        return Response(data=result.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer = RouterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk=None,ip=None):
        router = []
        if pk != None:
            router = self.get_object(pk=pk)
        elif ip != None:
            router = RouterDetails.objects.filter(status=1,loopback__exact=ip)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer = RouterSerializer(router,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        router = RouterDetails.objects.filter(pk=pk)
        router.update(status=0)
        return Response(status=status.HTTP_204_NO_CONTENT)
