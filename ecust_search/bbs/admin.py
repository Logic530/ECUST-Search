from django.contrib import admin
from .models import Section, Topic, Comment, Profile

admin.site.register(Section)
admin.site.register(Topic)
admin.site.register(Comment)
admin.site.register(Profile)
