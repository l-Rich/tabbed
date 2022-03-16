from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone

class Trip(models.Model):
    
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def total_costs(self):
        total = 0
        expenses = Activity.objects.filter(trip_id=self.id)
        for thing in expenses:
            total += thing.price
        return total
        
class Meta: 
    ordering = ['name']

class Traveler(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Lodging(models.Model):
    name= models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    max_occupants = models.IntegerField()
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name="lodging")
        
    def __str__(self):
        return self.name



class Activity(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name="activity")
    
    def __str__(self):
        return self.name
    

    
class FriendList(models.Model):
    user =models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user")
    friends = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="friends")

    def __str__(self):
        return self.user.username

    def add_friend(self, account):
        if not account in self.friends(all):
            self.friends.add(account)
            self.save()
    def remove_friend(self, account):
        if account in self.friends(all):
            self.friends.remove(account)
    
    def remove_friend(self, removed_friend):
        remover_friends_list = self
        remover_friends_list.remove_friend(removed_friend)
        friends_list = FriendList.objects.get(user=removed_friend)
        friends_list.remove_friend(self.user)

class FriendRequest(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="receiver")
    is_active = models.BooleanField(blank=True, null=False, default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender.username
    
    def accept(self):
        receiver_friend_list= FriendList.objects.get(user=self.receiver)
        if receiver_friend_list:
            receiver_friend_list.add_friend(self.sender)
            sender_friend_list = FriendList.objects.get(user=self.sender)
            if sender_friend_list:
                sender_friend_list.add_friend(self.receiver)
                self.is_active = False
                self.save()
    def decline(self):
        self.is_active= False
        self.save()
    def cancel(self):
        self.is_active = False
        self.save() 

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    friend_list = models.ForeignKey(FriendList, null=True, blank=True, on_delete=models.CASCADE)
    possible_friends = models.ForeignKey(FriendRequest, null=True, blank=True, on_delete=models.CASCADE)
    trips = models.ForeignKey(Trip, null=True, blank=True, on_delete=models.CASCADE)    
    bio = models.TextField(blank=True, max_length=500)
    profile_pic = models.TextField(blank=True)

    def __str__(self):
        return self.user.username