from django.contrib import admin
from .models import Section, Topic, Comment, Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
admin.site.register(Section)
admin.site.register(Topic)
admin.site.register(Comment)
admin.site.register(Profile)