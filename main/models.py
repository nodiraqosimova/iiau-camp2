from django.db import models


class Queue(models.Model):
    student = models.ForeignKey('edu.Student', on_delete=models.CASCADE)
    preferred = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name}"
