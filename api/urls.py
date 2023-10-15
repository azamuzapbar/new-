from django.urls import path
from django.contrib.auth.views import LoginView
from .view import StudentAPIList, TeacherAPIList

urlpatterns = [
    path('api/students/', StudentAPIList.as_view(), name='student-list'),
    path('api/teacher/', TeacherAPIList.as_view(), name='teacher-list'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
]
