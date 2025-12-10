"""
Проект - Менеджер задач
"""

from shlex import split
from commands.add import add_command
from commands.help import help_command
from tasks.tasks import Task


def main():

    tasks: list[Task] = []
    next_id = 1

    print('Task менеджер. help - для справки')
    while True:
        try:
            raw = input("> ").strip()
            parts = split(raw)
            cmd, args = parts[0], parts[1:]  # add name="aaaa"
            match cmd:
                case 'help':
                    help_command()
                case 'add':
                    add_command(tasks, args, next_id)
                case 'list':
                    pass
                case 'remove':
                    pass
                case 'edit':
                    pass
                case 'tags':
                    pass
                case 'exit':
                    break
                case _:
                    print('Неизвестная команда')
        except KeyboardInterrupt:
            print('\nЗавешение приложения')
            break
        except Exception as e:
            print(f'[ERROR]: {e}')


if __name__ == "__main__":
    # main()
    with open('notes.txt', 'w', encoding='utf-8') as f:
        f.write('Привет\n')
        f.write('Я записал')
    print('Завершено')
