from django.urls import include, path
from .views import *

app_name = 'applicant'

urlpatterns = [



    path("dashboard", ApplicantDashboard, name='applicant-dashboard'),   

]
