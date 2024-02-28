from django.urls import path
from .import views
# from .views import update_application_status

urlpatterns = [
    path ('create-job/', views.create_job, name='create-job'),
    path('update-job/<int:pk>/', views.update_job, name='update-job'),
    path('manage-jobs/', views.manage_jobs, name='manage-jobs'),
    path('apply-to-job/<int:pk>/', views.apply_to_job, name='apply-to-job'),
    path('all-applicants/<int:pk>/', views.all_applicants, name='all-applicants'),
    path('applied-jobs/', views.applied_jobs, name='applied-jobs'),
    # path('send-mail', views.index ,name='email-send'), # added for email send
    # path('update_application_status/<int:application_id>/', update_application_status, name='update_application_status'),
    # path('update_status/<int:applicant_id>/', views.update_status, name='update_status'),
]