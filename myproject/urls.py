"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import  settings
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage,name='home'),
    path('signup/',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('main/',views.MainPage,name='main'),
    path('logout/',views.LogoutPage,name='logout'),
    path('aboutus/',views.AboutusPage,name='aboutus'),
    path('demo/',views.demo,name='demo'),
    path('termscondition/',views.Termscondition,name='termscondition'),
    path('disclaimer/',views.Disclaimer,name='disclaimer'),
    path('PrivacyPolicy/',views.PrivacyPolicy,name='PrivacyPolicy'),
    path('contactus/',views.contactus,name='contactus'),
     path('createblog/',views.CreateBlog,name='createblog'),
     
    path('topict1/',views.topict1,name='topict1'),
    path('topict2/',views.topict2,name='topict2'),
    path('topict3/',views.topict3,name='topict3'),
    
    path('topich1/',views.topich1,name='topich1'),
    path('topich2/',views.topich2,name='topich2'),
    path('topich3/',views.topich3,name='topich3'),
    
    path('topice1/',views.topice1,name='topice1'),
    path('topice2/',views.topice2,name='topice2'),
    path('topice3/',views.topice3,name='topice3'),
    
    path('TechnologyInformation/',views.TechnologyInformation,name='Technology Information'),
    path('Hacking/',views.Hacking,name='Hacking'),
    path('EarnAway/',views.EarnAway,name='EarnAway'),
    path('EarnAway/',views.EarnAway,name='EarnAway'),
    
    
     
]

if settings.DEBUG:
    
    urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)