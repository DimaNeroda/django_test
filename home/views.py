from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from .models import *
import json


# Create your views here.


def home_default(request):
    return redirect('ua/')


def local_charts_teacher(request):

    # print(departments)

    data = request.GET

    id_teacher = data['id_teacher']
    current_language = data['current_language']

    timetable_list = TimeTable.objects.filter(IdTeacher__id=id_teacher)
    lecturehall_list = LectureHall.objects.all()
    timelesson_list = TimeLesson.objects.all()
    typesubject_list = TypeSubject.objects.all()

    nameLabel = []

    if current_language == "ru":
        nameLabel.append('Количество аудиторий')
        nameLabel.append('Количество пар по номеру')
        nameLabel.append('Количество пар по типам')
    elif current_language == "ua":
        nameLabel.append('Кількість аудиторій')
        nameLabel.append('Кількість занять за номером')
        nameLabel.append('Кількість занять за типом')
    else:
        nameLabel.append('Quantity of hall')
        nameLabel.append('Quantity of lessons by number')
        nameLabel.append('Quantity of lessons by type')

    numberHall = []
    countHallNH = []

    numberLesson = []
    countLessonNL = []

    typeSubject = []
    countLessonTS = []

    for hall in lecturehall_list:

        numberHall.append('№' + str(hall.NumberLectureHall))
        countHallNH.append(timetable_list.filter(IdLectureHall__id=hall.id).count())

    for time in timelesson_list:

        numberLesson.append('№' + str(time.NumberLesson))
        countLessonNL.append(timetable_list.filter(IdTimeLesson__id=time.id).count())

    if current_language == "ru":
        for typeS in typesubject_list:
            typeSubject.append(typeS.NameTypeSubject_ru)
            countLessonTS.append(timetable_list.filter(IdTypeSubject__id=typeS.id).count())
    elif current_language == "ua":
        for typeS in typesubject_list:
            typeSubject.append(typeS.NameTypeSubject_ua)
            countLessonTS.append(timetable_list.filter(IdTypeSubject__id=typeS.id).count())
    else:
        for typeS in typesubject_list:
            typeSubject.append(typeS.NameTypeSubject_en)
            countLessonTS.append(timetable_list.filter(IdTypeSubject__id=typeS.id).count())

    context = {}

    context['nameLabel'] = nameLabel

    context['numberHall'] = numberHall
    context['countHallNH'] = countHallNH

    context['numberLesson'] = numberLesson
    context['countLessonNL'] = countLessonNL

    context['typeSubject'] = typeSubject
    context['countLessonTS'] = countLessonTS

    return JsonResponse(json.dumps(context), safe=False)


def local_charts_group(request):

    data = request.GET

    id_department = data['id_department']
    id_group = data['id_group']
    current_language = data['current_language']

    timetable_list = TimeTable.objects.filter(IdDepartment__id=id_department,
                                              IdGroup__id=id_group)
    lecturehall_list = LectureHall.objects.all()
    timelesson_list = TimeLesson.objects.all()
    typesubject_list = TypeSubject.objects.all()

    nameLabel = []

    if current_language == "ru":
        nameLabel.append('Количество аудиторий')
        nameLabel.append('Количество пар по номеру')
        nameLabel.append('Количество пар по типам')
    elif current_language == "ua":
        nameLabel.append('Кількість аудиторій')
        nameLabel.append('Кількість занять за номером')
        nameLabel.append('Кількість занять за типом')
    else:
        nameLabel.append('Quantity of hall')
        nameLabel.append('Quantity of lessons by number')
        nameLabel.append('Quantity of lessons by type')

    numberHall = []
    countHallNH = []

    numberLesson = []
    countLessonNL = []

    typeSubject = []
    countLessonTS = []

    for hall in lecturehall_list:

        numberHall.append('№' + str(hall.NumberLectureHall))
        countHallNH.append(timetable_list.filter(IdLectureHall__id=hall.id).count())

    for time in timelesson_list:

        numberLesson.append('№' + str(time.NumberLesson))
        countLessonNL.append(timetable_list.filter(IdTimeLesson__id=time.id).count())

    if current_language == "ru":
        for typeS in typesubject_list:
            typeSubject.append(typeS.NameTypeSubject_ru)
            countLessonTS.append(timetable_list.filter(IdTypeSubject__id=typeS.id).count())
    elif current_language == "ua":
        for typeS in typesubject_list:
            typeSubject.append(typeS.NameTypeSubject_ua)
            countLessonTS.append(timetable_list.filter(IdTypeSubject__id=typeS.id).count())
    else:
        for typeS in typesubject_list:
            typeSubject.append(typeS.NameTypeSubject_en)
            countLessonTS.append(timetable_list.filter(IdTypeSubject__id=typeS.id).count())

    context = {}

    context['nameLabel'] = nameLabel

    context['numberHall'] = numberHall
    context['countHallNH'] = countHallNH

    context['numberLesson'] = numberLesson
    context['countLessonNL'] = countLessonNL

    context['typeSubject'] = typeSubject
    context['countLessonTS'] = countLessonTS

    return JsonResponse(json.dumps(context), safe=False)


def faculty(request):
    data = request.GET

    departments = Department.objects.filter(IdFaculty__id=data['id_faculty'])
    # print(departments)

    context = {}

    if data['current_language'] == "ru":
        for dep in departments:
            context[dep.id] = dep.NameDepartment_ru  # Locale
    elif data['current_language'] == "ua":
        for dep in departments:
            context[dep.id] = dep.NameDepartment_ua  # Locale
    else:
        for dep in departments:
            context[dep.id] = dep.NameDepartment_en  # Locale

    return JsonResponse(json.dumps(context), safe=False)


def course(request):
    data = request.GET

    groups = Group.objects.filter(IdCourse__id=data['id_course'])

    context = {}

    for grp in groups:
        context[grp.id] = grp.NumberGroup

    return JsonResponse(json.dumps(context), safe=False)


def department(request):
    data = request.GET

    teachers = Teacher.objects.filter(IdDepartment__id=data['id_department'])

    context = {}

    if data['current_language'] == "ru":
        for tch in teachers:
            SNP = tch.Surname_ru + ' ' + tch.Name_ru + ' ' + tch.Patronymic_ru  # Locale
            context[tch.id] = SNP
    elif data['current_language'] == "ua":
        for tch in teachers:
            SNP = tch.Surname_ua + ' ' + tch.Name_ua + ' ' + tch.Patronymic_ua  # Locale
            context[tch.id] = SNP
    else:
        for tch in teachers:
            SNP = tch.Surname_en + ' ' + tch.Name_en + ' ' + tch.Patronymic_en  # Locale
            context[tch.id] = SNP

    return JsonResponse(json.dumps(context), safe=False)


# def charts(request):
#     timetable_list = TimeTable.objects.all()
#     teacher_list = Teacher.objects.all()
#
#     doubleT = []
#
#     for tch in teacher_list:
#         teach = list()
#         teach.append(tch.Surname_ru + ' ' + tch.Name_ru[0] + '. ' + tch.Patronymic_ru[0] + '.')  # Locale
#         teach.append(timetable_list.filter(IdTeacher__id=tch.id).count())
#         doubleT.append(teach)
#
#     context = {}
#     nameT = []
#     countL = []
#
#     doubleT.sort(key=lambda x: x[1], reverse=True)
#
#     if len(doubleT) > 10:
#         for i in range(10):
#             nameT.append(doubleT[i][0])
#             countL.append(doubleT[i][1])
#     else:
#         for i in range(len(doubleT)):
#             nameT.append(doubleT[i][0])
#             countL.append(doubleT[i][1])
#
#     context['nameT'] = nameT
#     context['countL'] = countL
#
#     typesubject_list = TypeSubject.objects.all()
#
#     typeS = []
#     countS = []
#
#     for typSbj in typesubject_list:
#         typeS.append(typSbj.NameTypeSubject_ru)  # Locale
#         countS.append(timetable_list.filter(IdTypeSubject__id=typSbj.id).count())
#
#     context['typeS'] = typeS
#     context['countS'] = countS
#
#     return JsonResponse(json.dumps(context), safe=False)


def home_ru(request):
    data = request.GET
    scheduleFor = 'Nothing'
    if 'department' in data:
        if 'teacher' in data:
            filter_list = TimeTable.objects.filter(IdTeacher__id=data['teacher'])
            scheduleFor = 'Teacher'
            teacherFor = Teacher.objects.get(id=data['teacher'])
            # print("teacher")
        else:
            filter_list = TimeTable.objects.filter(IdDepartment__id=data['department'],
                                                   IdGroup__id=data['group'])
            scheduleFor = 'Group'
            departmentFor = Department.objects.get(id=data['department'])
            groupFor = Group.objects.get(id=data['group'])
            # print("student")
    else:
        filter_list = 0

    timetable_list = TimeTable.objects.all()
    subject_list = Subject.objects.all()
    dayweek_list = DayWeek.objects.all()
    week_list = Week.objects.all()
    timelesson_list = TimeLesson.objects.all()
    faculty_list = Faculty.objects.all()
    course_list = Course.objects.all()
    teacher_list = Teacher.objects.all()

    notLess = TimeTable()

    countWeek = Week.objects.all().count()
    countDay = DayWeek.objects.all().count()
    countLesson = TimeLesson.objects.all().count()

    allLess = []

    for w in range(countWeek):
        new_week = list()
        for l in range(countLesson):
            new_num_less = list()
            for d in range(countDay):
                new_num_less.append(notLess)
            new_week.append(new_num_less)
        allLess.append(new_week)

    typeDay = []

    for dw_in_l in dayweek_list:
        typeDay.append(dw_in_l.NameDay_ru)  # Locale

    typeWeek = []

    for w_in_l in week_list:
        typeWeek.append(w_in_l.TypeWeek_ru)  # Locale

    if filter_list == 0:
        pass
    else:
        for i in filter_list:
            allLess[typeWeek.index(i.IdWeek.TypeWeek_ru)][i.IdTimeLesson.NumberLesson - 1][
                typeDay.index(i.IdDayWeek.NameDay_ru)] = i  # Locale

    return render(request, 'ru/timetable/timetable.html', locals())  # Locale


def home_ua(request):
    data = request.GET
    scheduleFor = 'Nothing'
    if 'department' in data:
        if 'teacher' in data:
            filter_list = TimeTable.objects.filter(IdTeacher__id=data['teacher'])
            scheduleFor = 'Teacher'
            teacherFor = Teacher.objects.get(id=data['teacher'])
            # print("teacher")
        else:
            filter_list = TimeTable.objects.filter(IdDepartment__id=data['department'],
                                                   IdGroup__id=data['group'])
            scheduleFor = 'Group'
            departmentFor = Department.objects.get(id=data['department'])
            groupFor = Group.objects.get(id=data['group'])
            # print("student")
    else:
        filter_list = 0

    timetable_list = TimeTable.objects.all()
    subject_list = Subject.objects.all()
    dayweek_list = DayWeek.objects.all()
    week_list = Week.objects.all()
    timelesson_list = TimeLesson.objects.all()
    faculty_list = Faculty.objects.all()
    course_list = Course.objects.all()
    teacher_list = Teacher.objects.all()

    notLess = TimeTable()

    countWeek = Week.objects.all().count()
    countDay = DayWeek.objects.all().count()
    countLesson = TimeLesson.objects.all().count()

    allLess = []

    for w in range(countWeek):
        new_week = list()
        for l in range(countLesson):
            new_num_less = list()
            for d in range(countDay):
                new_num_less.append(notLess)
            new_week.append(new_num_less)
        allLess.append(new_week)

    typeDay = []

    for dw_in_l in dayweek_list:
        typeDay.append(dw_in_l.NameDay_ua)  # Locale

    typeWeek = []

    for w_in_l in week_list:
        typeWeek.append(w_in_l.TypeWeek_ua)  # Locale

    if filter_list == 0:
        pass
    else:
        for i in filter_list:
            allLess[typeWeek.index(i.IdWeek.TypeWeek_ua)][i.IdTimeLesson.NumberLesson - 1][
                typeDay.index(i.IdDayWeek.NameDay_ua)] = i  # Locale

    return render(request, 'ua/timetable/timetable.html', locals())  # Locale


def home_en(request):
    data = request.GET
    scheduleFor = 'Nothing'
    if 'department' in data:
        if 'teacher' in data:
            filter_list = TimeTable.objects.filter(IdTeacher__id=data['teacher'])
            scheduleFor = 'Teacher'
            teacherFor = Teacher.objects.get(id=data['teacher'])
            # print("teacher")
        else:
            filter_list = TimeTable.objects.filter(IdDepartment__id=data['department'],
                                                   IdGroup__id=data['group'])
            scheduleFor = 'Group'
            departmentFor = Department.objects.get(id=data['department'])
            groupFor = Group.objects.get(id=data['group'])
            # print("student")
    else:
        filter_list = 0

    timetable_list = TimeTable.objects.all()
    subject_list = Subject.objects.all()
    dayweek_list = DayWeek.objects.all()
    week_list = Week.objects.all()
    timelesson_list = TimeLesson.objects.all()
    faculty_list = Faculty.objects.all()
    course_list = Course.objects.all()
    teacher_list = Teacher.objects.all()

    notLess = TimeTable()

    countWeek = Week.objects.all().count()
    countDay = DayWeek.objects.all().count()
    countLesson = TimeLesson.objects.all().count()

    allLess = []

    for w in range(countWeek):
        new_week = list()
        for l in range(countLesson):
            new_num_less = list()
            for d in range(countDay):
                new_num_less.append(notLess)
            new_week.append(new_num_less)
        allLess.append(new_week)

    typeDay = []

    for dw_in_l in dayweek_list:
        typeDay.append(dw_in_l.NameDay_en)  # Locale

    typeWeek = []

    for w_in_l in week_list:
        typeWeek.append(w_in_l.TypeWeek_en)  # Locale

    if filter_list == 0:
        pass
    else:
        for i in filter_list:
            allLess[typeWeek.index(i.IdWeek.TypeWeek_en)][i.IdTimeLesson.NumberLesson - 1][
                typeDay.index(i.IdDayWeek.NameDay_en)] = i  # Locale

    return render(request, 'en/timetable/timetable.html', locals())  # Locale


class GetRequest(View):

    def get(self, request):
        data = request.GET
        filter_timetable_list = TimeTable.objects.filter(IdDepartment__id=data['department'],
                                                         IdGroup__id=data['group'])
        all_time_lesson_list = TimeLesson.objects.all()
        max_number_lesson = 0

        allSTThelp = {}
        allBFHhelp = {}
        allTWhelp = {}
        allDWhelp = {}

        allSTT = []
        allBFH = []
        allTW = []
        allDW = []

        all_return = {}
        mainTimeTableReturn = []
        for objectTimeTable in filter_timetable_list:
            if objectTimeTable.IdTimeLesson.NumberLesson > max_number_lesson:
                max_number_lesson = objectTimeTable.IdTimeLesson.NumberLesson

            idSTT = (objectTimeTable.IdSubject_id, objectTimeTable.IdTypeSubject_id, objectTimeTable.IdTeacher_id)
            if idSTT in allSTThelp:
                pass
            else:
                allSTThelp[idSTT] = 0
                getRequestSubjectTypeTeacherList = {
                    "id_name_subject": objectTimeTable.IdSubject_id,
                    "id_type_subject": objectTimeTable.IdTypeSubject_id,
                    "id_teacher": objectTimeTable.IdTeacher_id,
                    "name_subject": objectTimeTable.IdSubject.NameSubject_ua,
                    "type_subject": objectTimeTable.IdTypeSubject.NameTypeSubject_ua,
                    "surname_teacher": objectTimeTable.IdTeacher.Surname_ua,
                    "name_teacher": objectTimeTable.IdTeacher.Name_ua,
                    "patronymic_teacher": objectTimeTable.IdTeacher.Patronymic_ua
                }
                allSTT.append(getRequestSubjectTypeTeacherList)

            idBFH = (objectTimeTable.IdBuilding_id, objectTimeTable.IdLectureHall_id)
            if idBFH in allBFHhelp:
                pass
            else:
                allBFHhelp[idBFH] = 0
                getRequestBuildingFloorHallList = {
                    "id_building": objectTimeTable.IdBuilding_id,
                    "id_lecture_hall": objectTimeTable.IdLectureHall_id,
                    "number_building": objectTimeTable.IdBuilding.NumberBuilding,
                    "number_floor": objectTimeTable.IdLectureHall.NumberFloor,
                    "number_hall": objectTimeTable.IdLectureHall.NumberLectureHall
                }
                allBFH.append(getRequestBuildingFloorHallList)

            idTW = objectTimeTable.IdWeek_id
            if idTW in allTWhelp:
                pass
            else:
                allTWhelp[idTW] = 0
                getRequestTypeWeek = {
                    "id_type_week": objectTimeTable.IdWeek_id,
                    "type_week": objectTimeTable.IdWeek.TypeWeek_ua
                }
                allTW.append(getRequestTypeWeek)

            idDW = objectTimeTable.IdDayWeek_id
            if idDW in allDWhelp:
                pass
            else:
                allDWhelp[idDW] = 0
                getRequestDayWeek = {
                    "id_day_week": objectTimeTable.IdDayWeek_id,
                    "day_week": objectTimeTable.IdDayWeek.NameDay_ua
                }
                allDW.append(getRequestDayWeek)

            getRequestTimetableList = {
                "id_type_week": objectTimeTable.IdWeek_id,
                "id_day_week": objectTimeTable.IdDayWeek_id,
                "id_time_lesson": objectTimeTable.IdTimeLesson_id,
                "id_name_subject": objectTimeTable.IdSubject_id,
                "id_type_subject": objectTimeTable.IdTypeSubject_id,
                "id_building": objectTimeTable.IdBuilding_id,
                "id_lecture_hall": objectTimeTable.IdLectureHall_id,
                "id_teacher": objectTimeTable.IdTeacher_id,
                # "type_week": objectTimeTable.IdWeek.TypeWeek_ua,
                # "day_week": objectTimeTable.IdDayWeek.NameDay_ua,
                # "number_lesson": objectTimeTable.IdTimeLesson.NumberLesson,
                # "start_time": objectTimeTable.IdTimeLesson.StartTime,
                # "end_time": objectTimeTable.IdTimeLesson.EndTime,
                # "name_subject": objectTimeTable.IdSubject.NameSubject_ua,
                # "type_subject": objectTimeTable.IdTypeSubject.NameTypeSubject_ua,
                # "number_building": objectTimeTable.IdBuilding.NumberBuilding,
                # "number_floor": objectTimeTable.IdLectureHall.NumberFloor,
                # "number_hall": objectTimeTable.IdLectureHall.NumberLectureHall,
                # "surname_teacher": objectTimeTable.IdTeacher.Surname_ua,
                # "name_teacher": objectTimeTable.IdTeacher.Name_ua,
                # "patronymic_teacher": objectTimeTable.IdTeacher.Patronymic_ua
            }
            mainTimeTableReturn.append(getRequestTimetableList)

        allTL = []

        for i in all_time_lesson_list:
            if i.NumberLesson <= max_number_lesson:
                getRequestTimeLessonList = {
                    "id_time_lesson": i.id,
                    "number_lesson": i.NumberLesson,
                    "start_time": i.StartTime,
                    "end_time": i.EndTime
                }
                allTL.append(getRequestTimeLessonList)
        # print(len(allTL))

        all_return["MainTimeTable"] = mainTimeTableReturn
        all_return["TypeWeek"] = allTW
        all_return["DayWeek"] = allDW
        all_return["TimeLesson"] = allTL
        all_return["SubjectTypeTeacher"] = allSTT
        all_return["BuildingFloorHall"] = allBFH

        return JsonResponse(all_return, safe=False)
