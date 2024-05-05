import os
import sys
from colorama import Fore

def list_directory(path):
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_dir():
                    print(Fore.BLUE + f"📁 {entry.name}")
                else:
                    print(Fore.GREEN + f"📄 {entry.name}")
    except FileNotFoundError:
        print(Fore.RED + "Директорія не знайдена.")
    except PermissionError:
        print(Fore.RED + "Недостатньо прав для доступу до цієї директорії.")
    except Exception as e:
        print(Fore.RED + f"Виникла помилка: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Потрібно вказати лише шлях до директорії як аргумент командного рядка.")
    else:
        directory_path = sys.argv[1]
        print(Fore.YELLOW + f"Структура директорії {directory_path}:")
        list_directory(directory_path)