
from django.urls import path , include

from django.shortcuts import redirect

def home_redirect(request):
    return redirect('login') 

urlpatterns = [
    
]



