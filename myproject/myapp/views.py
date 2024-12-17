from django.shortcuts import render, get_object_or_404
from . models import Course
# Create your views here.


def c_list(request):
    return render(request, 'c_list.html', {'courses' : Course.objects.all()})
def ser_id(request):
    courses = Course.objects.filter(c_id__icontains = request.GET.get('c_id', ''))
    return render(request, 'ser_id.html', {'courses' : courses})


def ser_name(request):
    courses = Course.objects.filter(c_name__icontains = request.GET.get('c_name', ''))
    return render(request, 'ser_name.html', {'courses': courses})

def edit(request, c_id):
    course = get_object_or_404(Course, c_id = c_id)
    if request.method == 'POST':
        course.c_name = request.POST['c_name']
        course.save()
    return render(request, 'edit.html', {'course': course})

def delete(request):
    courses = []
    if 'c_id' in request.GET:
        c_id = request.GET['c_id']
        courses = Course.objects.filter(c_id__icontains = c_id)
    if request.method == 'POST':
        c_delete = request.POST.get('c_delete')
        if c_delete:
            course = get_object_or_404(Course, c_id = c_delete)
            course.delete()
    return render(request, 'delete.html', {'courses' : courses})