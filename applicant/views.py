from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from django.contrib.auth.forms import PasswordChangeForm
from foundation.decorators import *
from .forms import *
from .models import *
from django.contrib.messages.views import SuccessMessageMixin
import random



@login_required
@applicant_required
def ApplicantDashboard(request):
    return render(request, 'applicantdashboard.html')





def ApplicantProfile(request, pk):
    template_name = 'customer/editprofile.html'
    customer = get_object_or_404(PersonalDetails, pk=pk)
    form = SellerProfileForm(request.POST or None,
                             request.FILES or None, instance=customer)
    if request.method == 'POST':
        if form.is_valid():
            p = form.save(commit=False)
            p.save()
            messages.success(
                request, "Your Profile Was Updated Successfully...")
            return redirect('applicant:applicant-dashboard')
    return render(request, template_name, {'form': form})




def SellerProfile(request, pk):
    template_name = 'seller/sellerprofile.html'
    seller = get_object_or_404(PersonalDetails, pk=pk)
    form = SellerProfileForm(
        request.POST or None, request.FILES or None, instance=seller)
    if request.method == 'POST':
        if form.is_valid():
            p = form.save(commit=False)
            p.save()
            messages.success(
                request, "Your Profile Was Updated Successfully...")
            return redirect('applicant:dashboard')
    return render(request, template_name, {'form': form})


