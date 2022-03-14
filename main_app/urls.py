from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home.as_view(),name="home"),
    path('trips/',views.TripList.as_view(), name="trip_list"),
    path('trips/new/', views.TripCreate.as_view(), name="trip_create"),
    path('trips/<int:pk>/', views.TripDetail.as_view(), name="trip_detail"),
    path('trips/<int:pk>/activity/new', views.ActivityCreate.as_view(), name="activity_create"),
    path('accounts/signup/', views.Signup.as_view(), name="signup")
]