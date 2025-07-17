import os
import random
import time

SNOW_DENSITY = 10
DELAY = .3

SNOWFLAKES = ['❄', '❅', '❆', '❅', '❆', '❄️', '❇', '❈']

TERM = os.get_terminal_size()

TERMWIDTH = term.columns
TERMHEIGHT = term.lines

GRID = []

for _ in range(TERMHEIGHT):
  grid.append([' '] * TERMWIDTH)

def DRAW_GRID():
  os.system('clear')

  print('\033[?25l')

  output = ''

  for ROW in GRID:
    output += ''.join(ROW) + '\n'

  output = output.strip('\n')

  print(output, end='')

while True:
  row = []

  for _ in range(TERMWIDTH):
    if random.random() < SNOW_DENSITY / 100:
      row.append(random.choice(SNOWFLAKES))
    else:
      row.append(' ')

  grid.insert(0, row)
  grid.pop()
  
  DRAW_GRID()

  time.sleep(DELAY)
