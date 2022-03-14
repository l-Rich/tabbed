from django.contrib import admin
from .models import Trip, Lodging, Activity, FriendRequest, FriendList

admin.site.register(Trip)
admin.site.register(Lodging)
admin.site.register(Activity)
admin.site.register(FriendList)
admin.site.register(FriendRequest)

# Register your models here.
