from django.shortcuts import render
from item.models import Category, Item, Logo
from .models import *
from MR.models import Image
from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .helpers import send_forget_password_mail

def index(request):
    logos = Logo.objects.filter()[0:6]
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request,'MR/index.html',{
        'categories':categories,
        'items':items,
        'logos':logos,
        
    })
def contact(request):
    return render(request,'MR/contact.html',{
    })


# Create your views here.
def home(request):
    return render(request,"MR/index.html")
def singin(request):
    images = Image.objects.filter()[0:6]
    #Profile = Profile.objects.filter()[0:6] 
    if request.method == "POST":
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        #if not Email or not password:
            #messages.success(request,'Both Email and Password are required.')
            #return redirect('login')
        #user_obj = User.objects.filter(email=email).first()
        #if user_obj is None:
           # messages.success(request,'User not found.')
            #return redirect('/login/')
        if user:
            auth_user = authenticate(username=user.username, password=password)
            if auth_user:
                login(request, auth_user)
                return redirect('dashboard')
            else:
                print("mot de pass incorrecte")
        else:
            print("User does not exist")

    return render(request, 'MR/login.html', {
         'images':images,
         #'Profile':Profile
    })

def singup(request):
    error = False
    message = ""
    if request.method == "POST":
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        repassword = request.POST.get('repassword', None)
        # Email
        try:
            validate_email(email)
        except:
            error = True
            message = "Enter un email valide svp!"
        # password
        if error == False:
            if password != repassword:
                error = True
                message = "Les deux mot de passe ne correspondent pas!"
        # Exist
        user = User.objects.filter(Q(email=email) | Q(username=name)).first()
        if user:
            error = True
            message = f"Un utilisateur avec email {email} ou le nom d'utilisateur {name} exist déjà'!"
        
        # register
        if error == False:
            user = User(
                username = name,
                email = email,
            )
            user.save()

            user.password = password
            user.set_password(user.password)
            user.save()

            return redirect('singin')

            #print("=="*5, " NEW POST: ",name,email, password, repassword, "=="*5)

    context = {
        'error':error,
        'message':message
    }
    return render(request, 'MR/signup.html', context)


@login_required(login_url='singin')
def dashboard(request):
    return render(request, 'MR/index.html', {})

def logout(request):
    logout(request)
    return redirect('singin')

def ChangePassword(request):
    context = {}
    try:
        profile_obj = Profile.objects.get(forget_password_token = token)
        print(profile_obj)
    except Exception as e:
        print(e)
    return render(request,'MR/changepassword.html')
import uuid
def ForgetPassword(request):
    try:
        if request.methode == 'POST':
            email = request.POST.get('email')

            if not User.objects.filter(email=email).first():
                messages.success(request,'Not user found with this email.')
                return redirect('/forgetpassword/')
            user_obj = User.objects.get(email=email)
            token = str(uuid.uuid4())
            send_forget_password_mail(user_obj,token)
            massages.success(request,'An email is sent.')
            return redirect('/forgetpassword/')

    except Exception as e:
        print(e)
    return render(request,'MR/forgetpassword.html')
