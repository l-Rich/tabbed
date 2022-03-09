from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home.as_view(),name="home"),
    path('trips/',views.TripList.as_view(), name="trip_list")
]