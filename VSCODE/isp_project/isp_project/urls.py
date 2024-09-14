# isp_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('login')),  # Redirect root URL to login page
    path('admin/', admin.site.urls),  # Route for admin page
    path('', include('psb.urls')),  # Route for PSB app, root points to psb.urls
    #path('', lambda request: redirect('login')),  # Redirect root URL to login page

]


