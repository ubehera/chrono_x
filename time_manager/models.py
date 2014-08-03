# from django.db import models
# from django.contrib.auth.models import User, Group
from mongoengine import *
import datetime
from django.utils.timezone import utc

# Create your models here.

class Person(Document):
    first_name = StringField(max_length=20)
    last_name = StringField(max_length=20)

class Activity(EmbeddedDocument):
    name = StringField(max_length=50)
    description = StringField(max_length=50)

class Schedule(Document):
    # user = models.ForeignKey(User)
    activity = ListField(EmbeddedDocumentField(Activity))
    start_time = DateTimeField(help_text='start time')
    end_time = DateTimeField(help_text='end time')

