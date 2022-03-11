from django.shortcuts import render , redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.dates import DateDetailView
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.urls import reverse
from .models import Trip, Lodging, Activity 

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

class TripCreate(CreateView):
    model = Trip
    fields = ['name', 'country', 'state', 'city', 'date']
    template_name = "trip_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TripCreate, self).form_valid(form)
    
    def get_success_url(self):
        print(self.kwargs)
        # return reverse('trip_detail', kwargs={'pk': self.object.pk})

class TripDetail(DetailView):
    model = Trip
    template_name = "trip_detail.html"

class ActivityCreate(View):
    
    def post(self, request, pk):
        name = request.POST.get("name")
        price = request.POST.get("price")
        trip = Trip.objects.get(pk=pk)
        Activity.objects.create(name=name, price=price, trip=trip)
        return redirect ('trip_detail', pk=pk)
    
# class ActivityCreate(View):
    
#     def post(self, request, pk):
#         name = request.POST.get("name")
#         type = request.POST.get("type")
#         price = request.POST.get("price")
#         max_occupancy = request.POST.get("max")
#         trip = Trip.objects.get(pk=pk)
#         Activity.objects.create(name=name, type=type, price=price, max_occupancy=max_occupancy, trip=trip)
#         return redirect ('trips', pk=pk)
    
# Create your views here.
