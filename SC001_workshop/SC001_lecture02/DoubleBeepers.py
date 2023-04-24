"""
File: DoubleBeepers.py
Name:Laura Chiu
-------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will double the beepers
    """
    move()
    double_beepers()
    put_beeper_back()
    Karel_goes_home()

def double_beepers():
    while on_beeper():
        # old beeper,facing East.
        pick_beeper()
        move()
        put_beeper()
        put_beeper()
        # new beppers,facing East.
        turn_around()
        move()
        # old beppers,facing West.
        turn_around()


def turn_around():
    turn_left()
    turn_left()


def put_beeper_back():
    move()
    while on_beeper():
        pick_beeper()
        turn_around()
        move()
        put_beeper()
        turn_around()
        move()


def Karel_goes_home():
     turn_around()
     move()
     move()
     turn_around()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
