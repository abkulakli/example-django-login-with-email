from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomUserSerializer
from .permissions import Permission1Check, Permission2Check, Permission3Check


class CustomUserRegisterView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class AuthenticatedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response("You are authenticated")


class Permission1GrantedView(APIView):
    permission_classes = [Permission1Check]

    def get(self, request):
        return Response("You have permission1 so you can view this page")


class Permission2GrantedView(APIView):
    permission_classes = [Permission2Check]

    def get(self, request):
        return Response("You have permission2 so you can view this page")


class Permission3GrantedView(APIView):
    permission_classes = [Permission3Check]

    def get(self, request):
        return Response("You have permission3 so you can view this page")
