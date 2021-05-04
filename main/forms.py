from django import forms

from .models import Queue


class QueueForm(forms.ModelForm):
    student_cert = forms.CharField(label="Talabalik guvohnomasi seriyasi va raqamini kiriting",
                                   help_text="Masalan, K-1234567")
    phone = forms.CharField(label="Telefon raqamingizni kiriting", required=True)

    class Meta:
        model = Queue
        fields = ['student_cert']
