from django.contrib import admin
from .models import *


# Register your models here.


class FacultyAdmin(admin.ModelAdmin):  # создание класса на основе модели
    list_display = [field.name for field in Faculty._meta.fields]  # вывод всех полей

    class Meta:
        model = Faculty


admin.site.register(Faculty, FacultyAdmin)


class DepartmentAdmin(admin.ModelAdmin):  # создание класса на основе модели
    list_display = [field.name for field in Department._meta.fields]  # вывод всех полей

    class Meta:
        model = Department


admin.site.register(Department, DepartmentAdmin)


class CourseAdmin(admin.ModelAdmin):  # создание класса на основе модели
    list_display = [field.name for field in Course._meta.fields]  # вывод всех полей

    class Meta:
        model = Course


admin.site.register(Course, CourseAdmin)


class GroupAdmin(admin.ModelAdmin):  # создание класса на основе модели
    list_display = [field.name for field in Group._meta.fields]  # вывод всех полей

    class Meta:
        model = Group


admin.site.register(Group, GroupAdmin)


class WeekAdmin(admin.ModelAdmin):  # создание класса на основе модели
    list_display = [field.name for field in Week._meta.fields]  # вывод всех полей

    class Meta:
        model = Week


admin.site.register(Week, WeekAdmin)


class DayWeekAdmin(admin.ModelAdmin):  # создание класса на основе модели
    list_display = [field.name for field in DayWeek._meta.fields]  # вывод всех полей

    class Meta:
        model = DayWeek


admin.site.register(DayWeek, DayWeekAdmin)


class TimeLessonAdmin(admin.ModelAdmin):  # создание класса на основе модели
    list_display = [field.name for field in TimeLesson._meta.fields]  # вывод всех полей

    class Meta:
        model = TimeLesson


admin.site.register(TimeLesson, TimeLessonAdmin)


class TypeSubjectAdmin(admin.ModelAdmin):  # создание класса на основе модели
    list_display = [field.name for field in TypeSubject._meta.fields]  # вывод всех полей

    class Meta:
        model = TypeSubject


admin.site.register(TypeSubject, TypeSubjectAdmin)


class SubjectAdmin(admin.ModelAdmin):  # создание класса на основе модели
    list_display = [field.name for field in Subject._meta.fields]  # вывод всех полей

    class Meta:
        model = Subject


admin.site.register(Subject, SubjectAdmin)


class LectureHallAdmin(admin.ModelAdmin):  # создание класса на основе модели
    list_display = [field.name for field in LectureHall._meta.fields]  # вывод всех полей

    class Meta:
        model = LectureHall


admin.site.register(LectureHall, LectureHallAdmin)


class BuildingAdmin(admin.ModelAdmin):  # создание класса на основе модели
    list_display = [field.name for field in Building._meta.fields]  # вывод всех полей

    class Meta:
        model = Building


admin.site.register(Building, BuildingAdmin)


class TeacherAdmin(admin.ModelAdmin):  # создание класса на основе модели
    list_display = [field.name for field in Teacher._meta.fields]  # вывод всех полей

    class Meta:
        model = Teacher


admin.site.register(Teacher, TeacherAdmin)


class TimeTableAdmin(admin.ModelAdmin):  # создание класса на основе модели
    list_display = [field.name for field in TimeTable._meta.fields]  # вывод всех полей

    class Meta:
        model = TimeTable


admin.site.register(TimeTable, TimeTableAdmin)
