from django.urls import path
from . import views


urlpatterns = [
    path('student/',views.student_profile, name='student-profile'),
]