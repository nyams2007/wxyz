# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: SimpleLedger
def enable_colors():
    global _color_enabled
    _color_enabled = True

def disable_colors():
    global _color_enabled
    _color_enabled = False

def colorize(text, color):
    if _color_enabled:
        return f"\033[{color}m{text}\033[0m"
    return text

def green(text): return colorize(text, "32")
def red(text): return colorize(text, "31")
def yellow(text): return colorize(text, "33")
def cyan(text): return colorize(text, "36")
def bold(text): return colorize(text, "1")
def dim(text): return colorize(text, "2")
