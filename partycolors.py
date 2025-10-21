def new_func():
    def print_party_colors():
        BLUE = "\033[94m"
        RED = "\033[91m"
        RESET = "\033[0m"
    
        print(f"{BLUE}Democrats{RESET}")
        print(f"{RED}Republicans{RESET}")

    print_party_colors()

new_func()

