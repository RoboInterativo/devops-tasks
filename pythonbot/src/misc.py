def create_text_schedule(schedule, day):
    txt = ''
    txt += f'{day}\n'
    lessons = schedule[day]
    for lesson in lessons:
        txt += f'Дисциплина:        {lesson["Discipline"]}\n'
        txt += f'Кабинет:       {lesson["Classroom"]}\n'
        txt += f'Тип:       {lesson["Discipline_Type"]}\n'
        txt += f'Преподаватель:     {lesson["FIO_teacher"]}\n'
        txt += f'Время:     {lesson["TimeIn"][:5]} -- {lesson["TimeOut"][:5]} \n'
        txt += '_______________________________\n\n'
    if txt == f'{day}\n':
        return f'В {day} нет пар.'
    return txt
