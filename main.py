import sys
from time import sleep

def type(w, delay = 0.25, instant=False, newline=True):
  if instant == True and delay != 0:
    delay = 0
  for char in w:
    sys.stdout.write(char)
    sys.stdout.flush()
    sleep(delay)
  if newline == True:
    print("")
def rgbcolortype(w, r, g, b, delay=0.25, instant=False, newline=True):
  if instant == True and delay != 0:
    delay =0
  sys.stdout.write(f"\033[38;2;{r};{g};{b}m")
  sys.stdout.flush()
  for c in w:
    sys.stdout.write(c)
    sys.stdout.flush()
    sleep(delay)
  if newline == True:
    print("")
  print("\033[0m")