from django.shortcuts import render,redirect,get_object_or_404
from .models import Album,Track,Gallery,TrackByEmail,Vtrack,VerifyEmail,Event
from django.views.generic import ListView,DetailView
import os
from django.contrib import messages
import platform
from .forms import GetAlbumByEmailForm,ConfirmAndDownload,VerifyEmailForm
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.mail import send_mail
import random
import  re
import time
from datetime import datetime,date,time,timedelta
from email.message import EmailMessage
import smtplib
from gtts import gTTS 


GET_ALBUM_ID = 0
HAS_VISITED = False
USER_EMAIL = ""
USER_PLATFORM = ''
USER_SYSTEM =''

def home(request):
    return render(request,"blog/home.html")


def about(request):
    return render(request,"blog/about.html")


def album(request):
    albums = Album.objects.all().order_by('-date_posted')

    context = {
        'albums':albums,
    }

    return render(request,"blog/albums.html",context)

def album_detail(request,slug):
    album = get_object_or_404(Album,slug=slug)
    tracks  = Track.objects.filter(album=album).order_by('-date_posted')
    my_tracks = tracks.count()
    secret_download_key = random.randint(1,2000000)

    if request.method == "POST":
        form = GetAlbumByEmailForm(request.POST)
        if form.is_valid():
            useremail = form.cleaned_data.get('email')
            if TrackByEmail.objects.filter(email=useremail).exists():
                messages.info(request,f"Email already exist for a non-downloadable spot.")
            else:
                TrackByEmail.objects.create(email=useremail,album_title=album.slug,random_id=secret_download_key) 
                return HttpResponseRedirect(album.get_absolute_url_afteremail())

    else:
        form = GetAlbumByEmailForm()
    
    if album:
        album.views +=1
        album.save()

    context = {
        'album':album,
        'tracks':tracks,
        'track_count':my_tracks,
        'form':form
    }

    return render(request,"blog/album_track_detail.html",context)


def can_download(request):
    
    emailsent = False
    check_email = ""
    msg = EmailMessage()

    if request.method == "POST":
        form = VerifyEmailForm(request.POST)
        if form.is_valid():
            usersformemail = form.cleaned_data.get('youremail')

            if TrackByEmail.objects.filter(email=usersformemail).exists():
                VerifyEmail.objects.create(youremail = usersformemail)
                etrack_email = TrackByEmail.objects.get(email=usersformemail)
                ve = VerifyEmail.objects.get(youremail=usersformemail)
                your_album = etrack_email.album_title
                your_code = etrack_email.random_id
                album_link = f"127.0.0.1:8000/can_download_track/{your_album}/"
                msg["Subject"] = f"Dealpeepol welcomes you dearly."
                msg["From"] = settings.EMAIL_HOST_USER
                msg["To"] = usersformemail
                msg.set_content(
                    f"Thank you,this is a one-time link to download your album \n {your_album} and you may need the code below too.\nPlease copy this code {your_code } and follow this link {album_link}")
                hml = f"""
                <!Doctype html>
                <html>
                <body>
                <h1 style='font-style:italic;'>Dealpeepol welcomes you dearly.</h1>
                <p style='color:SlateGray;'> Thank you,this is a one-time link to download your album {your_album}.</p>
                <p style='color:SlateGray;'>And you may need the code below too</p>
                <p style='color:SlateGray;'>Please copy this code <strong>{your_code }</strong> and follow this link {album_link}</p>
                </body>
                </html>
                </html>
                """
                msg.add_alternative(hml, subtype='html')
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login(settings.EMAIL_HOST_USER,settings.EMAIL_HOST_PASSWORD)
                    smtp.send_message(msg)
                    
                    emailsent = True
                    uplatform = platform.platform()
                    your_code = random.randint(100,1000000)
                    uinfo = Vtrack.objects.create(user_code=your_code,user_platform=uplatform)
                    ve.delete()
                    check_email = "Please check your email now...."
            
            else:
                # ve.delete()
                messages.info(request,f"Your email does not exist.")
                # return redirect("albums")

    else:
        form = VerifyEmailForm()
    

    context = { 
        'check_email':check_email,
        'form':form,
        'emailsent':emailsent,
    }
    return render(request,"blog/candownload.html",context)

def can_download_tracks(request,slug):

    album = get_object_or_404(Album,slug=slug)
    tracks  = Track.objects.filter(album=album)
    my_tracks = tracks.count()
    email_code_confirmed = False


    if request.method == "POST":
        form = ConfirmAndDownload(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            code = form.cleaned_data.get('code')
            etrack_email = get_object_or_404(TrackByEmail,email=email)
            if TrackByEmail.objects.filter(email=email).exists() and TrackByEmail.objects.filter(random_id=code).exists():
                email_code_confirmed = True
                messages.success(request,f"Email and code confirmed successfully.")
                etrack_email.delete()
                return redirect('download_now',slug=slug)
            else:
                email_code_confirmed = False
                messages.info(request,f"Invalid details.")
                # return redirect("albums")
        else:
            messages.info(request,f"Invalid details")
    else:
        form = ConfirmAndDownload()


    context = {
        'album':album,
        'tracks':tracks,
        'track_count':my_tracks,
        'emai_code_confirmed':email_code_confirmed,
        'form':form,
    }

    return render(request,"blog/can_download_track.html",context)

def download_now(request,slug):

    album = get_object_or_404(Album,slug=slug)
    tracks  = Track.objects.filter(album=album)
    my_tracks = tracks.count()

    uplatform = platform.platform()
    
    has_visited = False
    # user_visited = get_object_or_404(Vtrack,user_platform=uplatform)
    user_visited = Vtrack.objects.get(user_platform=uplatform)
    user_visited_code = user_visited.user_code
    visit_count = user_visited.vcount
    if Vtrack.objects.filter(user_code=user_visited_code).exists() and Vtrack.objects.filter(user_platform=uplatform).exists() and visit_count == 0:
        has_visited = False
        user_visited.vcount = 1
        user_visited.save()
    else:
        has_visited = True
        user_visited.delete()
        return redirect('albums')
    

    context = {
        'album':album,
        'tracks':tracks,
        'track_count':my_tracks,
        'has_visited':has_visited
    }

    return render(request,"blog/download_now.html",context)

def album_detail_afteremail(request,slug):
    album = get_object_or_404(Album,slug = slug)
    tracks  = Track.objects.filter(album=album).order_by('-date_posted')
    my_tracks = tracks.count()

    context = {
        'album':album,
        'tracks':tracks,
        'track_count':my_tracks,
    }

    return render(request,"blog/album_detail_afteremail.html",context)

class GalleryView(ListView):
    model = Gallery
    template_name = 'blog/gallery.html'
    context_object_name = 'gallery'
    ordering = ['-date_posted']

def events(request):
    events = Event.objects.all().order_by('-date_posted')[:1]

    context = {
        'events': events
    }

    return render(request,"blog/events.html",context)
