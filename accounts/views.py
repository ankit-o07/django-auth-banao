from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate , logout
from django.contrib import messages
from .form import CustomUserCreationForm
from .models import CustomUser

def signup(request):

    if request.method == "POST":
        print("TES1")
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            print("TES2")
            user = form.save()
            auth_login(request, user)  
            messages.success(request, "Signup successful! Redirecting to dashboard...")
            if (user.user_type == "Patient"):
                return redirect('patient_dashboard')
            else:
                return redirect('doctor_dashboard')
        else :
            for field, error_list in form.errors.items():
                for error in error_list:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = CustomUserCreationForm()
    
    
    return render(request, 'accounts/signup.html', {'form': form})

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, "Login successful! Redirecting to dashboard...")
            if (user.user_type == "Patient"):
                return redirect('patient_dashboard')
            else:
                return redirect('doctor_dashboard')
        else:
            messages.error(request, "Invalid username or password.")

    if request.user.is_authenticated:  
        if request.user.user_type == "Patient":
            return redirect('patient_dashboard')
        else:
            return redirect('doctor_dashboard')
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

# def dashboard(request):
#     if request.user.is_authenticated:
#         if request.user.user_type == 'Doctor':
#             return render(request, 'doctor/dashboard.html', {'user': request.user})
#         else:
#             return render(request, 'patient/dashboard.html', {'user': request.user})
#     else:
#         return redirect('login')  
