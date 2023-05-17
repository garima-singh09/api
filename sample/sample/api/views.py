from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response

class GreetingView(APIView):
    def post(self, request):
        username = request.data.get('username')
        if username:
            message = f"Hello, {username}! Welcome to the API."
        else:
            message = "Please provide a username in the request body."

        response = Response({'message': message})
        response['X-Custom-Header'] = 'Custom Header Value'
        response['Cache-Control'] = 'no-cache'
        return response
