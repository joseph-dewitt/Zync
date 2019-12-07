import os
import requests

headers = {
    'X-Client-ID': os.getenv('WUNDER_ID'),
    'X-Access-Token': os.getenv('WUNDER_TOKEN')
}
print(headers)
url_root = "https://a.wunderlist.com/api/v1/"
s = requests.Session()
s.headers.update(headers)


def create_list(title):
    body = {
        'title': title
    }
    return s.post(f"{url_root}lists", body=body).json()


def get_lists():
    return s.get(f"{url_root}lists").json()


def get_list(list_id):
    return s.get(f"{url_root}lists/{list_id}").json()


def create_task(list_id, title, complete=None):
    body = {
        'list_id': list_id,
        'title': title
    }
    return s.post(f"{url_root}tasks", body=body).json()


def get_tasks(list_id):
    params = {'list_id': list_id}
    return s.get(f"{url_root}tasks", params=params).json()


def get_task(task_id):
    return s.get(f"{url_root}tasks/{task_id}").json()


def create_subtask(task_id, title, completed=None):
    body = {
        'task_id': task_id,
        'title': title
    }
    return s.post(f"{url_root}subtasks", body=body).json()


def get_subtasks(task_id):
    params = {'task_id': task_id}
    return s.get(f"{url_root}subtasks", params=params).json()


def get_subtask(subtask_id):
    return s.get(f"{url_root}subtasks/{subtask_id}").json()


def create_reminder(task_id, datetime):
    body = {
        'task_id': task_id,
        'date': datetime
    }
    return s.post(f"{url_root}reminders", body=body).json()


def get_task_reminder(task_id):
    params = {'task_id': task_id}
    return s.get(f"{url_root}reminders", params=params).json()


def get_list_reminders(list_id):
    params = {'list_id': list_id}
    return s.get(f"{url_root}reminders", params=params).json()


print(get_list_reminders(405738483))
