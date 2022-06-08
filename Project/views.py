from django.shortcuts import render
from rest_framework.views import APIView


class Default(APIView):
    def get(self, request):
        return render(request, 'User/../templates/Project/default.html')

    def post(self, request):
        return render(request, 'User/../templates/Project/default.html')
