from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home.as_view(),name="home"),
    path('trips/',views.TripList.as_view(), name="trip_list"),
    path('trips/new/', views.TripCreate.as_view(), name="trip_create"),    
    path('trips/<int:pk>/delete', views.TripDelete.as_view(), name="trip_delete"),    
    path('trips/<int:pk>/activity/delete', views.ActivityDelete.as_view(), name="activity_delete"),    
    path('trips/<int:pk>/', views.TripDetail.as_view(), name="trip_detail"),
    path('trips/<int:pk>/activity/new', views.ActivityCreate.as_view(), name="activity_create"),
    path('trips/<int:pk>/lodging/new', views.LodgingCreate.as_view(), name="lodging_create"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('profile/<int:pk>/', views.ProfilePage.as_view(), name="profile"),
    path('profile/new/', views.ProfileCreate.as_view(), name="user_profile_create"),
]