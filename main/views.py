# Create your views here.
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView

from edu.models import Student
from news.models import Slider
from .forms import QueueForm
from .models import Queue


class HomePage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        queues = Queue.objects.all()
        requested_students = queues.filter(is_accepted=False).count()
        accepted_students = queues.filter(is_accepted=True).count()
        galeries = Slider.objects.all()
        students = Student.objects.all().count()
        context["accepted"] = accepted_students
        context["students"] = students
        context["requested"] = requested_students
        context['galeries'] = galeries
        return context


class QueueView(CreateView):
    template_name = 'queue.html'
    form_class = QueueForm

    def post(self, request, *args, **kwargs):
        form = QueueForm()
        student_cert: str = request.POST.get('student_cert')
        student = Student.objects.filter(student_cert=student_cert.upper()).first()
        if not student:
            messages.error(request, "Bu talaba tizimda mavzud emas", extra_tags='alert alert-danger')
            return render(request, self.template_name, {'form': form})
        queue = Queue.objects.filter(student=student).first()
        if queue:
            messages.warning(request, "Siz avval so'rov yuborgansiz. Iltimos kuting.", extra_tags='alert alert-warning')
        else:
            queue = Queue(student=student)
            student.phone = request.POST.get('student_cert')
            student.save()
            queue.save()
            messages.success(request, "Siz navbatga kiritildingiz! Tez orada siz bilan bog'lanamiz",
                             extra_tags='alert alert-success')
        return render(request, self.template_name, {'form': form})


@login_required()
def queue_control(request):
    queues = Queue.objects.all()
    requested_students = queues.filter(is_accepted=False).count()
    accepted_students = queues.filter(is_accepted=True).count()
    students = Student.objects.all().count()
    print(students)
    context = {
        "requested_students": requested_students,
        "accepted_students": accepted_students,
        "students": students,
    }
    return render(request, 'queue_control.html', context)


@login_required
def requested_students(request):
    if request.method == "POST":
        data = request.POST
        queues = data.get('queues', None)
        if queues:
            Queue.objects.filter(id__in=queues).update(is_accepted=True)
            return redirect('main:queue_control')
    queues = Queue.objects.filter(is_accepted=False)
    context = {
        'queues': queues
    }
    return render(request, 'control/queue.html', context)


@login_required
def accepted_students(request):
    queues = Queue.objects.filter(is_accepted=True)
    context = {
        'queues': queues
    }
    return render(request, 'control/accepted.html', context)


@login_required
def students_in_system(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'control/students.html', context)