from django.contrib import admin
from home.models import Contact, Signup, Profile, Post
# Register your models here.

admin.site.register(Contact)
admin.site.register(Signup)
admin.site.register(Post)
admin.site.register(Profile)