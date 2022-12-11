from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name="logout"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('addShelter', views.addShelter, name="addShelter"),
    path('donate', views.donate, name="donate"),
    path('findShelter', views.findShelter, name="findShelter"),
    path('save', views.save, name="save"),
    path('unsave', views.unsave, name="unsave"),
    path('changeVacancy', views.changeVacancy, name="changeVacancy"),
    path('donated', views.donated, name="donated"),
]