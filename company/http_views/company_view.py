from typing import Dict, List
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse

class CompanyView(APIView):
    def get(self, request):
        return render(request, '<div>this is test</div>', {'title': 'Company Page'})
    def post(self, request):
        return
    def put(self, request):
        return
    def delete(self, request):
        return
