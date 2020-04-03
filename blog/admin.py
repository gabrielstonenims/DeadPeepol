from django.contrib import admin

from .models import Album,Track,Gallery,TrackByEmail,Vtrack,VerifyEmail,Event

admin.site.register(Album)
admin.site.register(Track)
admin.site.register(Gallery)
admin.site.register(TrackByEmail)
admin.site.register(Vtrack)
admin.site.register(VerifyEmail)
admin.site.register(Event)