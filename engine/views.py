# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
from django.contrib.auth import logout as auth_logout
from .models import proUsers, proRoles
from .decorators import login_required
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.conf import settings
from application.component.utils import generate_random_code
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse

def index(request):
    if 'user_id' in request.session:
        return redirect('dashboard')
    return render(request, 'backend/index.twig')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = proUsers.objects.get(userName=username)
            if not user.activate:
                return JsonResponse({'success': False, 'error': 'Account is not activated'})
            if check_password(password, user.password):
                request.session['user_id'] = user.id
                request.session['user_name'] = user.userName
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'error': 'Invalid password'})
        except proUsers.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'User does not exist'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

@login_required
def dashboard(request):
    return render(request, 'backend/dashboard/dashboard.twig')

def logout(request):
    if 'user_id' in request.session:
        auth_logout(request)
    return redirect('index')

@login_required
def users(request):
    userData = proUsers.objects.all()
    return render(request, 'backend/users/users.twig', {'userData': userData})

@login_required
def adduser(request):
    roles = proRoles.objects.all()
    return render(request, 'backend/users/adduser.twig', {'roles': roles})

@login_required 
def registeruser(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        role_id = request.POST.get('roleID')
        role = proRoles.objects.get(id=role_id)
        sessionID = generate_random_code()
        obj = proUsers(
            firstName=request.POST.get('firstName'),
            lastName=request.POST.get('lastName'),
            empID=request.POST.get('empID'),
            email=email,
            roleID=role,
            sessionID=sessionID,
            activate=False,
            sessionActivate=False
        )
        obj.save()
        password_set_link = request.build_absolute_uri(reverse('setPassword', args=[sessionID]))
        send_mail(
            'User Registration Confirmation',
            f'Please set your password by clicking the following link: {password_set_link}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        return redirect('users')
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

def setPassword(request, sessionID):
    try:
        user = proUsers.objects.get(sessionID=sessionID)
        if request.method == 'POST':
            username = request.POST.get('username')
            newPassword = request.POST.get('password')
            confirmPassword = request.POST.get('confirmPassword')
            if newPassword != confirmPassword:
                return render(request, 'setPassword.twig', {
                    'sessionID': sessionID,
                    'error': 'Passwords do not match!'
                })
            user.userName = username
            user.password = make_password(newPassword)
            user.activate = True
            user.sessionActivate = True
            user.sessionID = None
            user.save()
            return redirect('index')
        return render(request, 'backend/users/setPassword.twig', {'sessionID': sessionID})
    except proUsers.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Invalid session ID'})

@login_required  
def viewProfile(request, id):
    userData = get_object_or_404(proUsers, id=id)
    return render(request, 'backend/users/viewProfile.twig', {'userData': userData})