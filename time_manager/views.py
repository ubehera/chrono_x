from django.shortcuts import render
import mongoengine

# Create your views here.

user = authenticate(username='vagrant', password='vagrant')
assert isinstance(user, mongoengine.django.auth.user)

