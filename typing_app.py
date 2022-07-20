import time
import curses
from curses import window, wrapper
from typing import List

from backend.api.snippet import get_all_snippets, get_snippet, get_random_snippet
from backend.classes.words import Words
from backend.models.enums import Mode

def start_screen(stdscr: window) -> Mode:
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!")
    stdscr.addstr(1, 0, "Select an option")
    stdscr.addstr(2, 0, "1. Text Mode")
    stdscr.addstr(3, 0, "2. Code Mode")
    stdscr.refresh()
    while True:
        key = stdscr.getkey()
        if ord(key) == 49:
            return Mode.TEXT
        elif ord(key) == 50:
            return Mode.CODE
        else:
            stdscr.addstr(4, 0, "Please choose the numerical value of either option")
            continue


def display_text(stdscr: window, target: str, current: List, wpm: int = 0):
    stdscr.addstr(target)
    stdscr.addstr(f"\nWPM:{wpm}")
    line = 0
    

    for i, char in enumerate(current):
        col = i%curses.COLS
        if char == target[i]:
            color = curses.color_pair(1)
        else:
            color = curses.color_pair(2)
        stdscr.addstr(line, col, char, color)
        if i>0 and col==0:
            line+=1


def wpm_test(stdscr: window, mode: Mode = Mode.TEXT):
    if mode == Mode.CODE:
        target_text = get_random_snippet()
    else:
        word_parser = Words()
        target_text = word_parser.get(20)
    # print(get_all_snippets())
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round(len(current_text)*60/(time_elapsed*5))


        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue
        if ord(key) == 27:
            break
        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text):
                current_text.pop()
        elif len(current_text)<len(target_text):
            current_text.append(key)
    return wpm
            


def main(stdscr: window):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    while True:
        mode = start_screen(stdscr)
        wpm = wpm_test(stdscr, mode)
        stdscr.addstr(f"\nYou have completed the test!\nWPM: {wpm}\nPress any key to restart...")
        key = stdscr.getkey()

        if ord(key) == 27:
            break
    

wrapper(main)