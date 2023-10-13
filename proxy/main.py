# JaponêsLofy - INT V5
import random
from faker import Faker
from colorama import Fore, Style, init
import os
import time
from tqdm import tqdm

init(autoreset=True)

def progress_bar(title, seconds, progress):
    columns, _ = os.get_terminal_size()
    width = columns - 30
    completed_width = int(width * progress)
    bar = f"[{Fore.GREEN}{'-' * completed_width}{Style.RESET_ALL}{' ' * (width - completed_width)}] {int(progress * 100)}%"
    print(f"\r{Fore.RED}{title} {Style.RESET_ALL}{bar}", end="")
    time.sleep(seconds / width)

def generate_proxies():
    num_proxies = int(input("Com quantas proxies você deseja trabalhar: "))
    print("\nProxy Loading...\n")
    for i in range(21):
        progress = i / 20
        progress_bar("Progress", 7, progress)

    print(f"{Fore.RED}Proxy Loading complete.{Style.RESET_ALL}")

    fake = Faker()
    proxies = []

    for _ in range(num_proxies):
        ip = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
        porta = random.randint(8000, 9000)
        proxy = f"{ip}:{porta}"
        proxies.append(proxy)

    with open("proxies.txt", "w") as file:
        file.write("\n".join(proxies))

    print(f"{Fore.RED}Proxy Generation complete.{Style.RESET_ALL}")

def eliminate_duplicates():
    print("\nClone Delet\n")
    for i in range(21):
        progress = i / 20
        progress_bar("Progress", 7, progress)

    print(f"{Fore.RED}Clone Delet complete.{Style.RESET_ALL}")

def check_proxies():
    print_title("Checkin")
    
    with open("proxies.txt", "r") as file:
        proxies = file.read().splitlines()

    live_proxies = []
    dead_proxies = []
    
    with tqdm(total=len(proxies), desc="Checking Proxies", bar_format="{desc}: {percentage:3.0f}%") as progress:
        for proxy in proxies:
            progress.update(1)
            result = check_proxy(proxy)
            if result == "live":
                live_proxies.append(proxy)
            else:
                dead_proxies.append(proxy)

    print("\nLive Proxies:")
    for live_proxy in live_proxies:
        print(f"{Fore.GREEN}{live_proxy}{Style.RESET_ALL}")

    print("\nDead Proxies:")
    for dead_proxy in dead_proxies:
        print(f"{Fore.RED}{dead_proxy}{Style.RESET_ALL}")

    with open("lives.txt", "w") as file:
        file.write("\n".join(live_proxies))

    print(f"{Fore.YELLOW}Proxies adicionadas em lives.txt{Style.RESET_ALL}")

    input(f"Pressione qualquer tecla para encerrar o código")

def check_proxy(proxy):
# IMPLEMENTE SUA LÓGICA PARA CHECKAR AS PROXYS VÁLIDAS.
    return random.choice(["live", "dead"])

def print_title(title):
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"\n{Fore.RED}{title}{Style.RESET_ALL}\n")

generate_proxies()
eliminate_duplicates()
check_proxies()
