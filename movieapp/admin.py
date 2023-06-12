from django.contrib import admin
from . models import Rate,Comment,Favourite
# Register your models here.
admin.site.register(Rate)
admin.site.register(Comment)
admin.site.register(Favourite)