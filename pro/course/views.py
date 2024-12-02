from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView
from .models import Course
from django.urls import reverse_lazy
# Create your views here.
def AllCourse(request):
    courses = Course.objects.all()
    return render(request, 'courselist.html', {'mod': courses})

def CoursebyID(request):
    course_id = request.GET.get('course_id', '')
    courses = Course.objects.filter(id__icontains=course_id)
    return render(request, 'coursebyid.html', {'mod': courses})

def CoursebyName(request):
    course_name = request.GET.get('course_name', '')
    courses = Course.objects.filter(name__icontains=course_name)
    return render(request, 'coursebyname.html', {'mod': courses})

class CourseUpdateView(UpdateView):
    model = Course
    fields = '__all__'
    template_name = 'courseupdate.html'
    success_url = reverse_lazy('course-list')

class CourseDeleteView(DeleteView):
    model = Course
    template_name='coursedelete.html'
    success_url = reverse_lazy('course-list')