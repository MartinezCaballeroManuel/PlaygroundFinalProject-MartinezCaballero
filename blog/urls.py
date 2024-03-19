"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from registro.views import login_request, register, editProfile, ChangePassword
from django.contrib.auth.views import LogoutView


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.CreateBlog.as_view(), name = 'index'),
    path('pages/', views.ListBlog.as_view(), name = 'pages'),
    path('about/', views.about, name = 'about'),
    path('admin/', admin.site.urls),
    path('pages/<pk>/', views.DetailBlog.as_view(), name = 'detail'),
    path('pages/<pk>/editar', views.UpdateBlog.as_view(), name = 'edit'),
    path('pages/<pk>/borrar', views.DeleteBlog.as_view(), name = 'delete'),

    path('login/', login_request, name ='login'),
    path('register/', register, name = 'register'),
    path('logout/', LogoutView.as_view(template_name = 'logout.html'), name = 'logout'),
    path('editProfile/', editProfile, name = 'editProfile'),
    path('cambiarContrasenia/', ChangePassword.as_view(), name = 'changePassword'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)