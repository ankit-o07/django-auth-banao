
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

def home_redirect(request):
    return redirect('login') 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_redirect, name='home'),  
    path('accounts/',include("accounts.urls")),
    path("doctor/",include("doctor.urls")),
    path("patient/",include("patient.urls")),

]


# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)