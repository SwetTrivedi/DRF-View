"""
URL configuration for modelserializer project.

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
from api import views
from functionbasedview import views as v
from classbasedview import views as v1
from genericbasedview import views as v2
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',views.Studentapi.as_view()),
    path('hello/',v.hello_world),
    path('studentapi/',v.student_api),
    path('studentapi/<int:pk>/',v.student_api),
    path('classbasedstudent/',v1.StudentApi.as_view()),
    path('classbasedstudent/<int:pk>/',v1.StudentApi.as_view()),
    path('studentlist/',v2.StudentList.as_view()),
    path('studentcreate/',v2.StudentCreate.as_view()),
    path('studentretrieve/<int:pk>/',v2.StudentRetrive.as_view()),
    path('studentupdate/<int:pk>/',v2.StudentUpdate.as_view()),
    path('studentdestory/<int:pk>/',v2.StudentDestroy.as_view()),
]
