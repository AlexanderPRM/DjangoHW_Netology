from django.contrib import admin

from .models import Student, Teacher, TeacherStudents


class TeacherStudents(admin.TabularInline):
    model = TeacherStudents

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = (TeacherStudents,)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass
