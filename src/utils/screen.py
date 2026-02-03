import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def pause():
    input("Press Enter to continue...")

def get_current_time():
    return time.time()

def short_text_smart(text, width):
    if len(text) <= width:
        return text
    cut = text[:width - 3]
    if ' ' in cut:
        cut = cut.rsplit(' ', 1)[0]
    return cut + "..."

        