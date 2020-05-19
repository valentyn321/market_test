from django.contrib import admin
from django.urls import path

from django.contrib.auth.views import LoginView, LogoutView

from cart import views as crt_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', LoginView.as_view(template_name="auth/login.html"), name="login"),
    path('logout/', LogoutView.as_view(template_name="auth/logout.html"), name="logout"),

    path('create_product/', crt_views.ProductView.as_view(), name="create_product")
]
