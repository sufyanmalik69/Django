from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path("",v_home,name ='home'),
    path("about/",v_about,name="about"),
    path("contact/",v_contact,name="contact"),
    path("tracker/",v_tracker,name="tracker"),
    path("search/",v_search,name="search"),
    path("productview/",v_productview,name="productview"),
    path("checkout/",v_checkout,name="checkout"),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)