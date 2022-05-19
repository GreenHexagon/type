import sys
from time import sleep

def type(w, delay = 0.25, instant=False, newline=True):
  if instant == True:
    delay = 0
  for char in w:
    sys.stdout.write(char)
    sys.stdout.flush()
    sleep(delay)
  if newline == True:
    print("")