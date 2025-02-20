from django.shortcuts import redirect
from django.contrib import messages

def doctor_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.user_type == "Doctor":
            return view_func(request, *args, **kwargs)
        else:
            messages.error(request, "Access denied. Doctors only!")
            return redirect("login")
    return wrapper_func
