import curses

def show_help():
    return "Commands: "
def clear_screen():
    return ""
def show_info():
    return "Info: "

commands = {
    "help": show_help,
    "clear": clear_screen,
    "info": show_info
}
