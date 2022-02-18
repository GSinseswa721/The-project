from django .urls import path
from. import views

urlpatterns = [
path('', views.home, name="home"),

path('shop_grid_3_columns_sidebar.html', views.shop-grid-3-columns-sidebar, name="shop_grid_3_columns_sidebar")

]