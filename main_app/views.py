from os import PRIO_PROCESS
from django.shortcuts import render , redirect, get_object_or_404
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.dates import DateDetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from .models import Profile, Trip, Lodging, Activity, Profile, FriendList, FriendRequest 
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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
        return reverse('trip_list')

class TripDelete(DeleteView):
    model = Trip
    template_name = "trip_delete_confirmation.html"
    success_url = "/trips/"

class ActivityDelete(DeleteView):
    model = Activity
    template_name = "activity_delete_confirmation.html"
    success_url = "/trips/<int:pk>"

class TripDetail(DetailView):
    model = Trip
    template_name = "trip_detail.html"

class ActivityCreate(View):
    
    def post(self, request, pk):
        name = request.POST.get("name")
        price = request.POST.get("price")
        trip = Trip.objects.get(pk=pk)
        print(type(price))
        Activity.objects.create(name=name, price=price, trip=trip)
        return redirect ('trip_detail', pk=pk)
        
    def get_context_data(self, **kwargs):
        # users = Profile.objects.all()
        context = super(Activity, self).get_context_data(**kwargs)
        context['total_price']=Activity.objects.get(total_price=self.request.price)
        print(context)
        return context

class LodgingCreate(View):
    
    def post(self, request, pk):
        name = request.POST.get("name")
        type = request.POST.get("type")
        price = request.POST.get("price")
        max_occupants = request.POST.get("max_occupants")
        trip = Trip.objects.get(pk=pk)
        Lodging.objects.create(name=name, type=type, price=price, max_occupants=max_occupants, trip=trip)
        return redirect ('trip_detail', pk=pk)
    

    
class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form ssubmit validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("trip_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
class ProfilePage(TemplateView):
    model= User
    template_name='registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        # users = Profile.objects.all()
        context = super(ProfilePage, self).get_context_data(**kwargs)
        context['profile']=Profile.objects.get(user=self.request.user)
        print(context)
        # page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        # context["page_user"]= self.request.user
        return context

class ProfileCreate(CreateView):
    model = Profile
    fields = ['bio', 'profile_pic']
    template_name = "registration/user_profile_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProfileCreate, self).form_valid(form)
    
    def get_success_url(self):
        print(self.kwargs)