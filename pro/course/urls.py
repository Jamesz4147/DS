from django.urls import path
from .views import *
urlpatterns = [
    path('course/', AllCourse, name='course-list'),
    path('coursebyid', CoursebyID, name='course-by-id'),
    path('coursebyname', CoursebyName, name='course-by-name'),
    path('update/<str:pk>', CourseUpdateView.as_view(), name='course-update'),
    path('delete/<str:pk>', CourseDeleteView.as_view(), name='course-delete'),
]
