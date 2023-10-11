from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import userProfile
from django.core.mail import send_mail
from django.conf import settings
import random
from django.contrib.auth import update_session_auth_hash
# Create your views here.


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method =='POST':
        Firstname=request.POST.get('FirstName')
        LastName=request.POST.get('LastName')
        Username=request.POST.get('Username')
        email=request.POST.get('email')
        Password=request.POST.get('Password')
        ConfirmPassword=request.POST.get('ConfirmPassword')
        if len(Password)<8:
            messages.success(request, "Profile pass must be 8 character.")
        else:
            if Password:
                a = []
                b = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
                c = []
                d = ['&', '$', '#', '@', '*', '!', '_', '/', '-']
                for i in b:
                    if i in Password:
                        a.append(i)
                for i in d:
                    if i in Password:
                        c.append(i)
                if len(a)!=0 and len(c)!= 0:
                    if Password==ConfirmPassword:
                        if User.objects.filter(username=Username).exists():
                            messages.success(request, "Profile Username Already Taken.")
                        elif User.objects.filter(email=email).exists():
                            messages.success(request, "Profile Email Already Taken.")
                        else:
                            user=User.objects.create_user(first_name=Firstname,last_name=LastName,
                                                           username=Username,email=email,password=Password)
                            user.set_password(Password)
                            user.save()
                            messages.success(request, "Profile Created.")
                            return redirect('signin')
                    else:
                        messages.warning(request, "Profile Password not Matched.")
                else:
                    messages.warning(request, "enter minimum 1 number and 1 special character in your password.(1-9,@,$,/)")
                
    return render(request, 'accounts/Sign Up.html')

# authenticate,login,logout
def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            messages.success(request, 'User Login')
            return redirect('home')
        else:
            messages.warning(request, 'User Not Found')
            return redirect('signup')
    return render(request, 'accounts/Sign In.html')


def signout(request):
    logout(request)
    return redirect('signin')
    # return render(request, 'accounts/Sign In.html')
    
def forget_pass(request):
    otp = random.randint(1111111,9999999)
    if request.method == 'POST':
        email = request.POST.get('email')
        send_mail_registration(email, otp)
        user = User.objects.get(email=email)
        if user:
            prof = userProfile(user = user, otp = otp)
            prof.save()
        return redirect('verify_otp')
    return render(request, 'accounts/Forget_password.html')

def verify_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pass')
        otp = request.POST.get('otp')

        user = User.objects.get(email=email)
        if user:
            prof = userProfile.objects.get(user = user)
            if prof.otp == otp:
                user.set_password(password)
                user.save()
                update_session_auth_hash(request, user)
                messages.warning(request, "User Password Changed.")
                return redirect('signin')
            else:
                messages.warning(request, "Otp not matched Try again.")
    return render(request, 'accounts/verify_otp.html')



def send_mail_registration(email, otp):
    subject = "Account Verification otp"
    message = f'hi your verify otp is :  {otp}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)