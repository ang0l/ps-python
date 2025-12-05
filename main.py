"""
Проект - Менеджер задач
"""
import datetime
from commands.help import help_command


def main():
    print('Task менеджер. help - для справки')
    while True:
        try:
            raw = input("> ").strip()
            parts = raw.split()
            cmd, args = parts[0], parts[1:]  # add name="aaaa"
            match cmd:
                case 'help':
                    help_command()
                case 'add':
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
    now = datetime.datetime.now()
    # %Y - 2025 ГОД
    # %y - 25 год
    # %m - 12 месяц
    # %d - 05 день
    # %H - 07 час
    # %M - 12 минута
    # %S - 17 секунда
    print(now.strftime('%Y-%m-%d %H:%M:%S'))
    print(now.strftime('%Y/%m/%d'))

    s = '2025-12-05/07:41'
    dt = datetime.datetime.strptime(s, '%Y-%m-%d/%H:%M')
    print(dt)
