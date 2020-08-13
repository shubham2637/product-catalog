from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, re_path

from . import views

urlpatterns = [
    # ... the rest of your URLconf goes here ...
    path('', views.index, name='index'),
    path('productlist',views.productlist,name='productlisting'),
    path('signup', views.sign_up, name="signup"),
    path('login', LoginView.as_view(template_name='login.html'), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
    path('product/<int:id>', views.productdetail,name="productdetail"),
    ]