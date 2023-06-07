from django.contrib import admin
from .models import Newclient, Friend, Belonging, Borrowed

admin.site.register(Newclient)
admin.site.register(Belonging)
admin.site.register(Borrowed)
admin.site.register(Friend)

