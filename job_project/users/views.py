from unittest import loader
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User
from .form import RegisterUserForm
from resume.models import Resume
from company.models import Company
from django.core.mail import send_mail
from django.template import loader
# Create your views here.

# register applicant only
def register_applicant(request):
    if request.method == 'POST':
        form=RegisterUserForm(request.POST)
        if form.is_valid():
            var=form.save(commit=False)
            var.is_applicant=True
            var.first_name=var.first_name   # added
            var.last_name=var.last_name # added
            var.username=var.email
            var.save()
            Resume.objects.create(user=var)
            messages.info(request,"Your account has been created.  Please login")
            return redirect('login')
        else:
            messages.warning(request,"Something went wrong.")
            return redirect('register-applicant')
    else:
        form=RegisterUserForm()
        context={"form":form}
        return render(request,"users/register_applicant.html",context)
    
# register recruiter only
def register_recruiter(request):
    if request.method == 'POST':
        form=RegisterUserForm(request.POST)
        if form.is_valid():
            var=form.save(commit=False)
            var.is_recruiter=True
            var.first_name=var.first_name   # added
            var.last_name=var.last_name # added
            var.username=var.email
            var.save()
            Company.objects.create(user=var)
            messages.info(request,"Your account has been created. Please login")
            return redirect('login')
        else:
            messages.warning(request,"Something went wrong.")
            return redirect('register-recruiter')
    else:
        form=RegisterUserForm()
        context={"form":form}
        return render(request,"users/register_recruiter.html",context)
 
# login a user
def login_user(request):
    if request.method == "POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        user = authenticate(request, username=email, password=password)
        if user is not None and user.is_active:
            login(request,user)
            subject = "You're In! Job Portal Login Successful"

            # Include Application Status in the body
            body = f"Hello {request.user.first_name},\n\n"\
            "Welcome back to the Job Portal! We're delighted to see you again.\n"\
            "If you have any questions or need assistance, feel free to reach out.\n\n"\
            "Best regards,\n"\
            "Your Job Portal Team"
            

            # Personalized Greeting
            name = f'{request.user.first_name} {request.user.last_name}'

            # Include Company Logo or Branding
            # Add the logic to fetch the company logo or branding

            # Customize Signature
            signature ="Your Job Portal Team"

            # Load HTML email template
            html_message = loader.render_to_string(
                'email_sender_app/message01.html',
                {
                    'name': name,
                    'subject': subject,
                    'body': body,
                    'signature': signature,
                }
            )

            # Send email
            send_mail(
                subject,
                'You are lucky to receive this mail.',
                'dhill7228@gmail.com',  # Update this with your email
                [request.user.email,'tthamaraiselvan2002@gmail.com'],  # Use the user's email from the request
                # ['tthamaraiselvan2002@gmail.com','tdhanasekareee@gmail.com'],
                html_message=html_message,
                fail_silently=False,
            )

            messages.info(request, 'You  successfully Login')
            # return redirect('job-listing')
            return redirect('dashboard')
        
            # if request.user.is_applicant:
            #     return redirect('applicant-dashboard')
            # elif request.user.is_recruiter:
            #     return redirect('recruiter-dashboard')
            # else:
            #     return redirect('login')
            
        else:
            messages.warning(request,"Something went wrong")
            return redirect('login')
    else:
        return render(request,"users/login.html")
    
    
#logout a user

def logout_user(request):
    logout(request)
    messages.info(request,"Your session has ended.")
    return redirect('login')


