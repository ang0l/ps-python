"""
Проект - Менеджер задач
"""
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


main()
