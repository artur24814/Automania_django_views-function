"""new URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from automania import views
from accounts.views import login_view, logout_view, register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
    path('', views.homepage),
    path('search/', views.search_views),
    path('all_car/', views.all_car),
    path('createCar/', views.createCar),
    path('car/<int:id>/', views.carView),
    path('messeges/<int:id_user>/', views.messege),
    path('user-messeges/', views.user_messeges),
    path('update-car/<int:id>/', views.update_car),
    path('make-order/', views.make_order),
    path('your-order/', views.your_order),
    path('update-order/<int:id>/', views.update_order),
    path('your-posts/', views.your_posts),
    path('leaving-opinion/', views.leaving_opinion),
    path('opinions/', views.all_opinions),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
