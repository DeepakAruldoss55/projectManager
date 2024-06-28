# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.hashers import check_password
from django.contrib.auth import logout as auth_logout
from .models import proUsers, proRoles, clients, projectStatus, projects
from .decorators import login_required
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.conf import settings
from application.component.utils import generateRandomCode
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.utils import timezone

def index(request):
    if 'user_id' in request.session:
        return redirect('dashboard')
    return render(request, 'backend/index.html')

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
    return render(request, 'backend/dashboard/dashboard.html')

def logout(request):
    if 'user_id' in request.session:
        auth_logout(request)
    return redirect('index')

@login_required
def users(request):
    logged_in_user_id = request.session.get('user_id')
    userData = proUsers.objects.exclude(roleID=1)
    return render(request, 'backend/users/users.html', {'userData': userData})

@login_required
def adduser(request):
    roles = proRoles.objects.exclude(id=1)
    return render(request, 'backend/users/adduser.html', {'roles': roles})

@login_required 
def registeruser(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        role_id = request.POST.get('roleID')
        role = proRoles.objects.get(id=role_id)
        sessionID = generateRandomCode()
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
                return render(request, 'setPassword.html', {
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
        return render(request, 'backend/users/setPassword.html', {'sessionID': sessionID})
    except proUsers.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Invalid session ID'})

@login_required  
def viewProfile(request, id):
    userData = get_object_or_404(proUsers, id=id)
    return render(request, 'backend/users/viewProfile.html', {'userData': userData})

@login_required  
@csrf_exempt
def updateUser(request, id):
    user = get_object_or_404(proUsers, id=id)
    if request.method == 'POST':
        try:
            user.firstName = request.POST.get('firstName')
            user.lastName = request.POST.get('lastName')
            user.empID = request.POST.get('empID')
            user.email = request.POST.get('email')
            user.roleID = proRoles.objects.get(id=request.POST.get('roleID'))
            user.save()
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return render(request, 'backend/users/updateUser.html', {'user': user, 'roles': proRoles.objects.all()})

@csrf_exempt
def deleteUser(request, id):
    if request.method == 'DELETE':
        user = get_object_or_404(proUsers, id=id)
        user.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@login_required
def clientsList(request):
    clientsData = clients.objects.all()
    return render(request, 'backend/clients/clients.html', {'clientsData': clientsData})
   
@login_required
def addclient(request):
    return render(request, 'backend/clients/addclient.html')

login_required 
def registerclient(request):
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        if user_id is None:
            return JsonResponse({'success': False, 'error': 'User is not logged in'}, status=401)
        obj = clients(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            mobile=request.POST.get('mobile'),
            address=request.POST.get('address'),
            description=request.POST.get('description'),
            createdBy_id=user_id
        )
        obj.save()
        return redirect('clientsList')
    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)

@login_required  
def viewClient(request, id):
    clientsData = get_object_or_404(clients, id=id)
    return render(request, 'backend/clients/viewClient.html', {'clientsData': clientsData})

@login_required  
@csrf_exempt
def updateClient(request, id):
    client = get_object_or_404(clients, id=id)
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        if user_id is None:
            return JsonResponse({'success': False, 'error': 'User is not logged in'}, status=401)
        try:
            client.name = request.POST.get('name')
            client.email = request.POST.get('email')
            client.mobile = request.POST.get('mobile')
            client.address = request.POST.get('address')
            client.description = request.POST.get('description')
            client.updatedBy_id = user_id
            client.updatedDate= timezone.now()
            client.save()
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return render(request, 'backend/clients/updateClient.html', {'client': client})

@csrf_exempt
def deleteClient(request, id):
    if request.method == 'DELETE':
        user = get_object_or_404(clients, id=id)
        user.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@login_required
def projectsList(request):
    projectStatusData = projectStatus.objects.all()
    clientsData = clients.objects.all()
    if request.method == 'POST':
        userID = request.session.get('user_id')
        if userID is None:
            return JsonResponse({'success': False, 'error': 'User is not logged in'}, status=401)
        obj = projects(
            projectNumber=request.POST.get('projectNumber'),
            name=request.POST.get('projectName'),
            projectDescription=request.POST.get('projectDescription'),
            projectStatus_id=request.POST.get('projectStatus'),
            clientID=request.POST.get('client'),
            projectUniqueID=generateRandomCode(),
            createdBy_id=userID
        )
        obj.save()
    return render(request, 'backend/projects/index.html', {'projectStatusData': projectStatusData, 'clientsData': clientsData})

