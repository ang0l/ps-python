"""Модуль для отметки задачи сделанной"""
from tasks.tasks import Task, find_task
from helpers.table import stringify_table


def done_command(tasks: list[Task], args: list[str]):
    if not args:
        print('Использование: done <id>')
        return

    try:
        task_id = int(args[0])
    except ValueError:
        print('[ERROR]: id должен быть числом')
        return

    task = find_task(tasks, task_id)
    if not task:
        print(f'Задача {task_id} не найдена')
        return

    if task['status'] == 'new':
        task['status'] = 'done'
    elif task['status'] == 'done':
        task['status'] = 'new'

    print(stringify_table([task]))
