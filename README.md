def print_colored_text(color):
    # ANSI escape codes for red and blue
    colors = {
        "red": "\033[31m",
        "blue": "\033[34m",
        "reset": "\033[0m"
    }
    
    if color.lower() == "red":
        print(f"{colors['red']}This is red text!{colors['reset']}")
    elif color.lower() == "blue":
        print(f"{colors['blue']}This is blue text!{colors['reset']}")
    else:
        print("Invalid color. Please choose 'red' or 'blue'.")

# Example usage
print_colored_text("red")
print_colored_text("blue")
