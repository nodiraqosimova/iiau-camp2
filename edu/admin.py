from django.contrib import admin

from edu import models


class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'first_name',
        'last_name',
        'group',
    ]
    list_filter = [
        'group',
    ]


admin.site.register(models.Faculty)
admin.site.register(models.Department)
admin.site.register(models.Group)
admin.site.register(models.Student, StudentAdmin)
