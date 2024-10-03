from shop_app.models import Shop
from .models import  Group

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .forms import RegisterForm, EditProfileForm
from .models import CustomUser


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            avatar = form.cleaned_data['avatar']
            password = form.cleaned_data['password']
            user = CustomUser.objects.create_user(username=username,
                                                  first_name=first_name,
                                                  last_name=last_name,
                                                  email=email,
                                                  phone_number=phone_number,
                                                  avatar=avatar,
                                                  password=password)
            user.set_password(password)
            user.save()

            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def profile_view(request):
    data = CustomUser.objects.get(id=request.user.id)
    if data.role == 'teacher':
        groups = Group.objects.filter(teacher=request.user)

        return render(request, 'teacher_profile.html', {'data': data, 'groups':groups})
    return render(request, 'profile.html', {'data': data})

def group_detail_view(request, id):
    group = Group.objects.get(id=id)
    students = CustomUser.objects.filter(group=group, role='student')
    return render(request, 'group_detail.html', {'group': group,'students': students})


def edit_profile_view(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})



@csrf_exempt
def add_coins_view(request, id):
    if request.method == 'POST':
        try:
            user = CustomUser.objects.get(id=id)
            coin = int(request.POST.get('coin', 0))
            user.coins += coin
            user.save()
            return JsonResponse({'success': True, 'new_coins': user.coins})
        except CustomUser.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'User not found'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})


def buy_product_view(request, id):
    student = CustomUser.objects.get(id=request.user.id)
    product = Shop.objects.get(id=id)
    if product.count > 0:
        if student.coins >= product.price:
            student.coins -= product.price
            student.save()
            product.count -= 1
            product.save()
            return redirect('home')
        else:
            message = "Sizda koinlar yetarli emas"
            return render(request, 'index.html', {'message': message})
    else:
        message = "Maxsulot qolmagan"
        return redirect('home', {'message': message})
