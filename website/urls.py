from django .urls import path
from. import views

urlpatterns = [
path('', views.home, name="home"),
path('about-us.html', views.about_us, name="about_us"),
path('contact-us.html', views.contact_us, name="contact_us"),
path('track-order.html',views.track_order, name="track_order")
]