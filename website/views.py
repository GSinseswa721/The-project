from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def about_us(request):
    return render(request, 'about-us.html', {})
def contact_us(request):
    return render(request, 'contact-us.html', {})
def track_order(request):
    return render(request, 'track-order.html', {})

