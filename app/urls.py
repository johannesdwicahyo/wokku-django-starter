from django.contrib import admin
from django.http import HttpResponse
from django.urls import path


def home(request):
    return HttpResponse("Wokku Django starter — it works. Edit app/urls.py to add your routes.")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
]
