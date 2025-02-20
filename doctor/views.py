from django.shortcuts import render
from .decorators import doctor_required
from django.contrib.auth.decorators import login_required


@login_required
@doctor_required
def dashboard(request):
    return render(request , "doctor/dashboard.html",{"user": request.user})