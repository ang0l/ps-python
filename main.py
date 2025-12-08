"""
Проект - Менеджер задач
"""
from datetime import datetime
from zoneinfo import ZoneInfo
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
    now_utc = datetime.now(ZoneInfo("UTC"))
    now = datetime.now()
    print(now_utc)
    print(now)

    now_ny = datetime.now(ZoneInfo('America/New_York'))
    print(now_ny)

    meeting = datetime(2025, 12, 8, 12,0, tzinfo=ZoneInfo('Europe/Moscow'))
    meeting_ny = meeting.astimezone(ZoneInfo('America/New_York'))
    print(meeting_ny)