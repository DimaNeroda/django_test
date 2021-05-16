from django.db import models

# Create your models here.


# Locale
class Faculty(models.Model):
    # Id = models.IntegerField(max_length=100, blank = True, null = True, default = None)
    NameFaculty_ru = models.CharField(max_length=200, blank=True, null=True, default=None)
    NameFaculty_ua = models.CharField(max_length=200, blank=True, null=True, default=None)
    NameFaculty_en = models.CharField(max_length=200, blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.NameFaculty_ru  # презентует(отображает) объекты базы данных по выбраным полям

    class Meta:
        verbose_name = 'Факультет'  # переопределение имени таблицы базы данных в единственном числе
        verbose_name_plural = 'Факультети'  # * во множественном числе


# Locale
class Department(models.Model):
    # Id = models.IntegerField(max_length=100, blank = True, null = True, default = None)
    NameDepartment_ru = models.CharField(max_length=200, blank=True, null=True, default=None)
    NameDepartment_ua = models.CharField(max_length=200, blank=True, null=True, default=None)
    NameDepartment_en = models.CharField(max_length=200, blank=True, null=True, default=None)
    IdFaculty = models.ForeignKey(Faculty, related_name='relDepartments', blank=True,
                                  null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return "Каф. %s, фак. %s" % (self.NameDepartment_ru,
                                     self.IdFaculty.NameFaculty_ru)  # презентует(отображает) объекты базы данных по выбраным полям

    class Meta:
        verbose_name = 'Кафедра'  # переопределение имени таблицы базы данных в единственном числе
        verbose_name_plural = 'Кафедри'  # * во множественном числе


class Course(models.Model):
    # Id = models.IntegerField(max_length=100, blank = True, null = True, default = None)
    NumberCourse = models.IntegerField()

    def __str__(self):
        return "%s" % self.NumberCourse  # презентует(отображает) объекты базы данных по выбраным полям

    class Meta:
        verbose_name = 'Курс'  # переопределение имени таблицы базы данных в единственном числе
        verbose_name_plural = 'Курси'  # * во множественном числе


class Group(models.Model):
    # Id = models.IntegerField(max_length=100, blank = True, null = True, default = None)
    NumberGroup = models.IntegerField()
    IdCourse = models.ForeignKey(Course, blank=True, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return "Группа №%s" % self.NumberGroup  # презентует(отображает) объекты базы данных по выбраным полям

    class Meta:
        verbose_name = 'Група'  # переопределение имени таблицы базы данных в единственном числе
        verbose_name_plural = 'Групи'  # * во множественном числе


# Locale
class Week(models.Model):
    # Id = models.IntegerField(max_length=100, blank = True, null = True, default = None)
    TypeWeek_ru = models.CharField(max_length=2, blank=True, null=True, default=None)
    TypeWeek_ua = models.CharField(max_length=2, blank=True, null=True, default=None)
    TypeWeek_en = models.CharField(max_length=2, blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.TypeWeek_ru  # презентует(отображает) объекты базы данных по выбраным полям

    class Meta:
        verbose_name = 'Тип тижня'  # переопределение имени таблицы базы данных в единственном числе
        verbose_name_plural = 'Типи тижнів'  # * во множественном числе


# Locale
class DayWeek(models.Model):
    # Id = models.IntegerField(max_length=100, blank = True, null = True, default = None)
    NameDay_ru = models.CharField(max_length=20, blank=True, null=True, default=None)
    NameDay_ua = models.CharField(max_length=20, blank=True, null=True, default=None)
    NameDay_en = models.CharField(max_length=20, blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.NameDay_ru  # презентует(отображает) объекты базы данных по выбраным полям

    class Meta:
        verbose_name = 'День неділі'  # переопределение имени таблицы базы данных в единственном числе
        verbose_name_plural = 'Дні неділі'  # * во множественном числе


class TimeLesson(models.Model):
    # Id = models.IntegerField(max_length=100, blank = True, null = True, default = None)
    NumberLesson = models.IntegerField()
    StartTime = models.TimeField()
    EndTime = models.TimeField()

    def __str__(self):
        return "№%s; %s-%s" % (self.NumberLesson,
                               self.StartTime,
                               self.EndTime)  # презентует(отображает) объекты базы данных по выбраным полям

    class Meta:
        verbose_name = 'Час заняття'  # переопределение имени таблицы базы данных в единственном числе
        verbose_name_plural = 'Час занять'  # * во множественном числе


# Locale
class Subject(models.Model):
    # Id = models.IntegerField(max_length=100, blank = True, null = True, default = None)
    NameSubject_ru = models.CharField(max_length=100, blank=True, null=True, default=None)
    NameSubject_ua = models.CharField(max_length=100, blank=True, null=True, default=None)
    NameSubject_en = models.CharField(max_length=100, blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.NameSubject_ru  # презентует(отображает) объекты базы данных по выбраным полям

    class Meta:
        verbose_name = 'Предмет'  # переопределение имени таблицы базы данных в единственном числе
        verbose_name_plural = 'Предмети'  # * во множественном числе


# Locale
class TypeSubject(models.Model):
    # Id = models.IntegerField(max_length=100, blank = True, null = True, default = None)
    NameTypeSubject_ru = models.CharField(max_length=50, blank=True, null=True, default=None)
    NameTypeSubject_ua = models.CharField(max_length=50, blank=True, null=True, default=None)
    NameTypeSubject_en = models.CharField(max_length=50, blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.NameTypeSubject_ru  # презентует(отображает) объекты базы данных по выбраным полям

    class Meta:
        verbose_name = 'Тип предмета'  # переопределение имени таблицы базы данных в единственном числе
        verbose_name_plural = 'Типи предметів'  # * во множественном числе


class LectureHall(models.Model):
    # Id = models.IntegerField(max_length=100, blank = True, null = True, default = None)
    NumberFloor = models.IntegerField()
    NumberLectureHall = models.IntegerField()

    def __str__(self):
        return "%s" % self.NumberLectureHall  # презентует(отображает) объекты базы данных по выбраным полям

    class Meta:
        verbose_name = 'Аудиторія'  # переопределение имени таблицы базы данных в единственном числе
        verbose_name_plural = 'Аудиторії'  # * во множественном числе


class Building(models.Model):
    # Id = models.IntegerField(max_length=100, blank = True, null = True, default = None)
    NumberBuilding = models.IntegerField(default=1)

    def __str__(self):
        return "%s" % self.NumberBuilding  # презентует(отображает) объекты базы данных по выбраным полям

    class Meta:
        verbose_name = 'Корпус'  # переопределение имени таблицы базы данных в единственном числе
        verbose_name_plural = 'Корпуси'  # * во множественном числе


# Locale
class Teacher(models.Model):
    # Id = models.IntegerField(max_length=100, blank = True, null = True, default = None)
    Surname_ru = models.CharField(max_length=100, blank=True, null=True, default=None)
    Surname_ua = models.CharField(max_length=100, blank=True, null=True, default=None)
    Surname_en = models.CharField(max_length=100, blank=True, null=True, default=None)
    Name_ru = models.CharField(max_length=100, blank=True, null=True, default=None)
    Name_ua = models.CharField(max_length=100, blank=True, null=True, default=None)
    Name_en = models.CharField(max_length=100, blank=True, null=True, default=None)
    Patronymic_ru = models.CharField(max_length=100, blank=True, null=True, default=None)
    Patronymic_ua = models.CharField(max_length=100, blank=True, null=True, default=None)
    Patronymic_en = models.CharField(max_length=100, blank=True, null=True, default=None)
    IdDepartment = models.ForeignKey(Department, blank=True, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s %s" % (self.Surname_ru,
                             self.Name_ru,
                             self.Patronymic_ru)  # презентует(отображает) объекты базы данных по выбраным полям

    class Meta:
        verbose_name = 'Викладач'  # переопределение имени таблицы базы данных в единственном числе
        verbose_name_plural = 'Викладачі'  # * во множественном числе


class TimeTable(models.Model):
    # Id = models.IntegerField(max_length=100, blank = True, null = True, default = None)
    IdDepartment = models.ForeignKey(Department, blank=True, null=True, default=None, on_delete=models.CASCADE)
    IdGroup = models.ForeignKey(Group, blank=True, null=True, default=None, on_delete=models.CASCADE)
    IdWeek = models.ForeignKey(Week, blank=True, null=True, default=None, on_delete=models.CASCADE)
    IdDayWeek = models.ForeignKey(DayWeek, blank=True, null=True, default=None, on_delete=models.CASCADE)
    IdTimeLesson = models.ForeignKey(TimeLesson, blank=True, null=True, default=None, on_delete=models.CASCADE)
    IdSubject = models.ForeignKey(Subject, blank=True, null=True, default=None, on_delete=models.CASCADE)
    IdTypeSubject = models.ForeignKey(TypeSubject, blank=True, null=True, default=None, on_delete=models.CASCADE)
    IdBuilding = models.ForeignKey(Building, blank=True, null=True, default=None, on_delete=models.CASCADE)
    IdLectureHall = models.ForeignKey(LectureHall, blank=True, null=True, default=None, on_delete=models.CASCADE)
    IdTeacher = models.ForeignKey(Teacher, blank=True, null=True, default=None, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id  # презентует(отображает) объекты базы данных по выбраным полям

    class Meta:
        verbose_name = 'Розклад'  # переопределение имени таблицы базы данных в единственном числе
        verbose_name_plural = 'Розклади'  # * во множественном числе

