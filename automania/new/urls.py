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
    path('', views.homepage, name='homepage'),
    #accounts
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
    path('search/', views.search_views, name='search_views'),
    path('all_car/', views.all_car, name='all_car'),
    path('createCar/', views.create_car, name='create_car'),
    path('car/<int:id>/', views.car_detail, name='car_detail'),
    #messages
    path('messeges/<int:id_user>/', views.messege),
    path('answer-messeges/<int:id_user>/<int:id_message>/', views.answer_to_messege),
    path('user-messeges/', views.user_messeges),
    path('delete_message/<int:id_message>/', views.delete_message),
    #CRUD for order
    path('make-order/', views.make_order),
    path('your-order/', views.your_order),
    path('update-order/<int:id>/', views.update_order),
    #CRUD for post
    path('your-posts/', views.your_posts, name='your_posts'),
    path('update-car/<int:id>/', views.update_car),
    #opinion
    path('leaving-opinion/', views.leaving_opinion),
    path('opinions/', views.all_opinions),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
