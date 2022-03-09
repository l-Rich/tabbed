from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.dates import DateDetailView
from .models import Trip 

class Home(TemplateView):
    template_name= "home.html"

# class Trip:
#     def __init__(self, name, country, state, city, date):
#         self.name= name
#         self.country = country
#         self.state = state
#         self.city = city
#         self.date = date
# trips = [
#     Trip("Girls Trip", "USA", "Florida", "Miami", "June 6, 2022" ), 
#     Trip("Family Vacation", "USA", "Texas", "Houston", "June 6, 2022"), 
#     Trip("Anniversary", "USA", "California", "Los Angeles", "June 6, 2022")
# ]

class TripList(TemplateView):
    template_name= "trip_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["trips"]=Trip.objects.filter(
                name__icontains=name, user=self.request.user)
            context["header"] = f"Searching for {name}"
        else:
            context["trips"] = Trip.objects.filter(user=self.request.user)
            context["header"] = "Upcoming Trips" 
        return context
# Create your views here.
