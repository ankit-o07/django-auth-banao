from django.shortcuts import render
from .decorators import patient_required
from django.contrib.auth.decorators import login_required

@login_required
@patient_required
def dashboard(request):
    return render(request , "patient/dashboard.html",{"user": request.user})