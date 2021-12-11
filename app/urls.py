from django.urls import include, path
from .views import *

#app_name = 'applicant'

urlpatterns = [



    path("", home, name='index'),
    path("login", login, name='user-login'),
    path('logout', logout_user, name='user-logout'),
    path('applicant/', ApplicantSignUp.as_view(), name='applicant-signup'),
    path('subadmin/', subAdminSignUp.as_view(), name='subadmin-signup'),   



]

