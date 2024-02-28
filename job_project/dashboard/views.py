from django.shortcuts import render, redirect

# Create your views here.

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')




# def proxy(request):
#     if request.user.is_applicant:
#         return redirect('applicant-dashboard')
#     elif request.user.is_recruiter:
#         return redirect('recruiter-dashboard')
#     else:
#         return redirect('login')
    
# def applicant_dashboard(request):
#     return render(request,'dashboard/applicant_dashboard.html')

# def recruiter_dashboard(request):
#     return render(request,'dashboard/recruiter_dashboard.html')
