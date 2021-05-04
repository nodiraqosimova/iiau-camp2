from django.urls import path

from main.views import QueueView, queue_control, HomePage, requested_students, accepted_students, students_in_system

app_name = 'main'
urlpatterns = [
    path('', HomePage.as_view(), name='base'),
    path('queue/', QueueView.as_view(), name='queue'),
    path('control/', queue_control, name='queue_control'),
    path('control/requested/', requested_students, name='requested_students'),
    path('control/accepted/', accepted_students, name='accepted_students'),
    path('control/students/', students_in_system, name='students_in_system'),
]
