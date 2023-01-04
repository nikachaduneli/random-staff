from django.contrib.auth import views as auth_views
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.add_applicant, name='add_applicant'),
    path('applicants/', views.applicants_list, name='applicants_list'),
    path('update_applicant/', views.update_applicant, name='update_applicant'),
    path('update_applicants_list/', views.update_applicants_list, name='update_applicants_list'),
    path('delete_applicants/', views.delete_applicants, name='delete_applicans'),
   
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
