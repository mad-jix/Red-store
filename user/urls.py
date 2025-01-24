from django.urls import path
from .import views


urlpatterns = [

    path('',views.index,name='index'),
    path('account/',views.account,name='account'),
    path('logout/', views.sign_out,name='logout'),
    path('profile-creation/', views.profile_creation, name='profile-creation'),

]
