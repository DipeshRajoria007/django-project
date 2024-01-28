from typing import Dict, List
from users.models import Users
from rest_framework.views import APIView
from django.http import JsonResponse

class UsersView(APIView):

    def get(self, request):
        request_data: Dict = request.query_params
        user_id: int = request_data.get('id')
        if not user_id:
            raise Exception('No user id provided')
        user: Dict = Users.objects.filter(id=user_id).first()
        if not user:
            raise Exception('Invalid user id provided')
        return_data: Dict = dict(id=user.id, name=user.name, email=user.email)
        return JsonResponse(return_data)

    def post(self, request):
        request_data: Dict = request.data
        name: str = request_data.get('name')
        username: str = request_data.get('username')
        email: str = request_data.get('email')
        password: str = request_data.get('password')
        if not name or not username or not email or not password:
            raise Exception('Params Missing!')
        new_user: Users = Users.objects.create(name=name, username=username, email=email, password=password)
        return JsonResponse({'id': new_user.id})

    def put(self, request):
        return

    def delete(self, request):
        return
