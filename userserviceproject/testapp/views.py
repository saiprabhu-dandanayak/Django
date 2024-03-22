from django.http import JsonResponse, HttpRequest, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone
from datetime import timedelta
from .models import User
from .serializers import UserSerializer
from .auth import create_jwt_token, ACCESS_TOKEN_EXPIRE_MINUTES
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import Http404

def home_page(request: HttpRequest) -> HttpResponse:
    return JsonResponse({"message": "Welcome to the homepage"})


def get_all_users(request: HttpRequest) -> HttpResponse:
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False)


def get_user_by_id(request: HttpRequest, user_id: int) -> HttpResponse:
    try:
        user = User.objects.get(id=user_id)
    except ObjectDoesNotExist:
        return JsonResponse({"detail": "User not found"}, status=404)
    serializer = UserSerializer(user)
    return JsonResponse(serializer.data)

def get_user_by_email(request: HttpRequest, email: str) -> HttpResponse:
    try:
        user = User.objects.get(email=email)
    except ObjectDoesNotExist:
        return JsonResponse({"detail": "User not found"}, status=404)
    serializer = UserSerializer(user)
    return JsonResponse(serializer.data)


@csrf_exempt
def create_user(request: HttpRequest) -> JsonResponse:
    if request.method == 'POST':
        data = json.loads(request.body)
        print(">>>>>>>>>>>>>", data)
        email = data.get('email')
        name = data.get('name')
        password = data.get('password')

        if User.objects.filter(email=email).exists():
            return JsonResponse({"detail": "Email already registered"}, status=400)

        hashed_password = make_password(password)
        user = User.objects.create(email=email, name=name, password=hashed_password)

        serializer = UserSerializer(user)
        return JsonResponse(serializer.data, status=201)
    else:
        return JsonResponse({"detail": "Unsupported request method"}, status=405)

@csrf_exempt 
def sign_in_user(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:  
            return JsonResponse({"detail": "Invalid credentials"}, status=401)

        if not check_password(password, user.password):
            return JsonResponse({"detail": "Invalid credentials"}, status=401)

        expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES) 
        jwt_token = create_jwt_token({"sub": user.email}, expires_delta)
        return JsonResponse({"token": jwt_token}, status=200)


@transaction.atomic
@csrf_exempt
def update_user(request: HttpRequest, user_id: int) -> HttpResponse:
    user = get_object_or_404(User, id=user_id)
    
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"detail": "Invalid JSON format"}, status=400)
    
    user.email = data.get('email', user.email)
    user.password = make_password(data.get('password', user.password))
    user.name = data.get('name', user.name)
    user.save()
    serializer = UserSerializer(user)
    return JsonResponse(serializer.data)


@csrf_exempt
@transaction.atomic
def change_password(request: HttpRequest) -> JsonResponse:
    if request.method == 'PATCH':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"detail": "Invalid JSON format"}, status=400)
        
        email = data.get('email')
        new_password = data.get('password')

        if not email or not new_password:
            return JsonResponse({"detail": "Email and password must be provided."}, status=400)

        user = get_object_or_404(User, email=email)
        user.password=make_password(new_password)
        user.save()

        return JsonResponse({"message": "Password changed successfully"})
    else:
        return JsonResponse({"detail": "Invalid request method"}, status=405)


@transaction.atomic
@csrf_exempt
def delete_user_by_id(request: HttpRequest, user_id: int) -> HttpResponse:
    try:
        user = get_object_or_404(User, id=user_id)
        user.delete()
        return JsonResponse({"message": "User deleted successfully"})
    except Http404:
        return JsonResponse({"detail": "User does not exist."}, status=404)


@transaction.atomic
def delete_all_users(request: HttpRequest) -> HttpResponse:
    User.objects.all().delete()
    return JsonResponse({"message": "All users deleted successfully"})
