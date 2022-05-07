from django.urls import path

from . import views

app_name = 'online_service'

urlpatterns = [
    path('', views.index, name='index'),
    path('recipe/', views.recipe, name='recipe'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('follow/', views.follow_index, name='follow_index'),
]
