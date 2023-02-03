from django.urls import path 
from . import views

urlpatterns=[
    path("", views.signup,name='signup'),
    path("login/", views.login,name='login'),
    path("shop", views.index,name='shop'),
    path("about/",views.about,name="AboutUs"),
    path("contact/",views.contact,name="ContactUs"),
    path("tracker/",views.tracker,name="TrackingStatus"),
    path("search/",views.search,name="Search"),
    path("products/<int:myid>",views.productview,name="Productview"),
    path("checkout/",views.checkout,name="Checkout"),


]
