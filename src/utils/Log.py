from colorama import Style, Fore


def info(message):
    print(f"{Style.BRIGHT}{Fore.GREEN}[INFO] {Style.RESET_ALL}{message}")


def warn(message):
    print(f"{Style.BRIGHT}{Fore.YELLOW}[WARN] {Style.RESET_ALL}{message}")


def error(message):
    print(f"{Style.BRIGHT}{Fore.RED}[REPORT] {Style.RESET_ALL}{message}")
