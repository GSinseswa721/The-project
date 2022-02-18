from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def shopgrid_3_columns_sidebar(request):
    return render(request, 'shop_grid_3_columns_sidebar.html', {})

