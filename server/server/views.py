from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
import json

class CustomLogoutView(LogoutView):
    """Custom logout view that shows confirmation page"""
    template_name = 'registration/logged_out.html'
    next_page = None  # Don't redirect, show the template

@csrf_exempt
@require_http_methods(["POST"])
def api_login(request):
    """API endpoint for user login"""
    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return JsonResponse({
                'status': 'error',
                'message': 'Username and password are required'
            }, status=400)
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return JsonResponse({
                'status': 'success',
                'message': 'Login successful',
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': user.email
                }
            })
        else:
            return JsonResponse({
                'status': 'error',
                'message': 'Invalid username or password'
            }, status=401)
            
    except json.JSONDecodeError:
        return JsonResponse({
            'status': 'error',
            'message': 'Invalid JSON data'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': 'An error occurred during login'
        }, status=500)

@csrf_exempt
@require_http_methods(["POST"])
def api_logout(request):
    """API endpoint for user logout"""
    try:
        logout(request)
        return JsonResponse({
            'status': 'success',
            'message': 'Logout successful',
            'redirect_url': '/'
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': 'An error occurred during logout'
        }, status=500)

@csrf_exempt
@require_http_methods(["POST"])
def api_register(request):
    """API endpoint for user registration"""
    try:
        data = json.loads(request.body)
        username = data.get('username')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        password = data.get('password')
        
        # Validation
        errors = {}
        
        if not username:
            errors['username'] = 'Username is required'
        elif User.objects.filter(username=username).exists():
            errors['username'] = 'Username already exists'
            
        if not first_name:
            errors['first_name'] = 'First name is required'
            
        if not last_name:
            errors['last_name'] = 'Last name is required'
            
        if not email:
            errors['email'] = 'Email is required'
        elif User.objects.filter(email=email).exists():
            errors['email'] = 'Email already exists'
            
        if not password:
            errors['password'] = 'Password is required'
        elif len(password) < 6:
            errors['password'] = 'Password must be at least 6 characters'
        
        if errors:
            return JsonResponse({
                'status': 'error',
                'errors': errors
            }, status=400)
        
        # Create user
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        
        return JsonResponse({
            'status': 'success',
            'message': 'Registration successful',
            'user': {
                'id': user.id,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email
            }
        })
        
    except json.JSONDecodeError:
        return JsonResponse({
            'status': 'error',
            'message': 'Invalid JSON data'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': 'An error occurred during registration'
        }, status=500)