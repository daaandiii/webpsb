from django.urls import path
from . import views

# Import the views for the relevant routes
from .views import pemasangan_list, psb_view, tambah_pemasangan
#login
from django.contrib.auth import views as auth_views

from django.urls import path
from .views import tambah_maintenance




urlpatterns = [
    #login
    path('login/', auth_views.LoginView.as_view(template_name='psb/login.html'), name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user/list/', views.user_list, name='user_list'),  # Assuming user list view exists
    path('profile/', views.profile_view, name='profile'),  # Tambahkan ini
    # List of pemasangan
    path('listpsb/', pemasangan_list, name='pemasangan_list'),
    
    # Main PSB view
    #path('psb/', psb_view, name='psb'),
    path('maintenance/', views.tambah_maintenance, name='maintenance_tambah'),
    path('psb/', views.tambah_pemasangan, name='psb'),

    #logout
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    #path('maintenance/tambah/', views.tambah_maintenance, name='tambah_maintenance'),
    path('listmaintenance/', views.maintenance_list, name='maintenance_list'),

    # Add new pemasangan
    #path('psb/tambah-pemasangan/', tambah_pemasangan, name='tambah_pemasangan'),


]
