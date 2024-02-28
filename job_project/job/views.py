from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import Job, ApplyJob
from .form import CreateJobForm, UpdateJobForm
# Create your views here.
from django.core.mail import send_mail
from django.template import loader

# create a job
def create_job(request):
    if request.user.is_recruiter and request.user.has_company:
        if request.method == 'POST':
            form = CreateJobForm(request. POST)
            if form.is_valid():
                var = form.save(commit=False)
                var.user = request.user
                var.company = request.user.company
                var.save()
                messages.info (request, 'New job has been created')
                return redirect('dashboard')
            else:
                messages.warning (request, 'Something went wrong')
                return render('create-job')
        else:
            form = CreateJobForm()
            context = {'form' : form}
            return render (request, 'job/create_job.html', context)
    else:
        messages.warning(request, 'Permission Denied')
        return redirect('dashboard')
    
# update  a job 
def update_job(request,pk):
    job=Job.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateJobForm(request. POST, instance=job)
        if form.is_valid():
            form.save()
            messages.info (request, 'Your job info is updated')
            return redirect('dashboard')
        else:
            messages.warning (request, 'Something went wrong')
    else:
        form = UpdateJobForm(instance=job)
        context = {'form' : form}
        return render (request, 'job/update_job.html', context)
    

def manage_jobs (request):
    jobs = Job.objects.filter(user=request.user, company=request.user.company)
    context = {'jobs': jobs}
    return render (request, 'job/manage_jobs.html', context)

def apply_to_job(request, pk):
    if request.user.is_authenticated and request.user.is_applicant:
        job = Job.objects.get(pk=pk)
        if ApplyJob.objects.filter(user=request.user, job=pk).exists():
            messages.warning(request, 'Permission Denied')
            return redirect('dashboard')
        else:
            application = ApplyJob.objects.create(
                job=job,
                user=request.user,
                status='Pending'
            )
            # Dynamic Subject Line
            subject = f'Congratulations! You have successfully applied for the position of {job.job_title} at {job.company.company_name}'

            # Include Application Status in the body
            body = f'You successfully applied for the position of "{job.job_title}" at "{job.company.company_name}". ' \
                   f'Your application status is currently "{application.status}". ' \
                   f'For more details, please log in to your Wob portal and check the dashboard.'

            # Personalized Greeting
            name = f'{request.user.resume.first_name} {request.user.resume.last_name}'

            # Include Company Logo or Branding
            # Add the logic to fetch the company logo or branding

            # Customize Signature
            signature = f'{job.company.rec_first_name} {job.company.rec_last_name}, Recruiter at {job.company.company_name}. ' \
                        'Feel free to reach out if you have any questions!'

            # Load HTML email template
            html_message = loader.render_to_string(
                'email_sender_app/message.html',
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

            messages.info(request, 'You have successfully applied! Please see dashboard')
            return redirect('job-listing')
    else:
        messages.info(request, 'Please log in to continue')
        return redirect('login')


def all_applicants(request, pk):
    job = Job.objects.get(pk=pk)
    applicants = job.applyjob_set.all()
    context = {'job': job, 'applicants': applicants}
    return render(request, 'job/all_applicants.html', context)


def applied_jobs(request):
    jobs = ApplyJob.objects.filter(user=request.user)
    context = {'jobs': jobs}
    return render(request, 'job/applied_job.html', context)



