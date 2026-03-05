from django.urls import path
from .views import job_list, job_page
from .views import upload_resume

urlpatterns = [
    path('jobs/', job_list),
    path('jobs-page/', job_page),
     path('upload-resume/', upload_resume),
]