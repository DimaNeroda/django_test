from django import template

register = template.Library()


@register.filter
def return_start_time(same_list, i):

    return same_list[int(i)].StartTime


@register.filter
def return_end_time(same_list, i):

    return same_list[int(i)].EndTime


@register.filter
def return_number(same_list, i):

    return same_list[int(i)].NumberLesson


@register.filter
def return_week_ru(same_list, i):  # Locale

    return same_list[int(i)].TypeWeek_ru


@register.filter
def return_week_ua(same_list, i):  # Locale

    return same_list[int(i)].TypeWeek_ua


@register.filter
def return_week_en(same_list, i):  # Locale

    return same_list[int(i)].TypeWeek_en


@register.filter
def return_id_tab_week(week, word):  # Locale

    return str(word) + str(week)


@register.filter
def return_concat_words(word1, word2):  # Locale

    return str(word1) + str(word2)
