from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class RegisterView(APIView):
    def post(self,request):
        serializer=RegisterSerializer(
            data=request.data
        )
        if serializer.is_valid():
           user= serializer.save()
           return Response(
               {
                   "message":"user create sucsesfuly"
               },
               status=201
           )
        return Response(
            serializer.errors,
            status=400
        )

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
         return Response({
             "username":request.user.username,
             "email":request.user.email
         })
