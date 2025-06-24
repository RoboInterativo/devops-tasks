import requests


def get_group_id(group_name: str):
    url = 'http://schedule.mslu.by/backend/buttonClicked?facultyId=221&educationForm=1'

    data = requests.get(url).json()
    groups_data = data['data']
    for group_data in groups_data:
        if group_data['Name'] == group_name:
            return group_data['IdGroup']


def get_group_schedule_current_week(group_id):
    url = f'http://schedule.mslu.by/backend/?groupId={group_id}&weekType=currentWeek'
    data = requests.get(url).json()['data']
    schedule = {
        'Понедельник': [],
        'Вторник': [],
        'Среда': [],
        'Четверг': [],
        'Пятница': [],
        'Суббота': [],
    }
    for day in data:
        schedule[day['Day']].append(day)

    return schedule
