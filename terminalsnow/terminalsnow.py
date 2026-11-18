import os
import random
import time

SNOW_DENSITY = 3
DELAY = 0.3
SNOWFLAKES = ['❄', '❅', '❆', '❇', '❈']

term = os.get_terminal_size()
TERMWIDTH = term.columns
TERMHEIGHT = term.lines

grid = []
for _ in range(TERMHEIGHT):
    grid.append([' '] * TERMWIDTH)

def draw_grid():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\033[?25l', end='')
    output = '\n'.join(''.join(row) for row in grid)
    print(output, end='', flush=True)

try:
    while True:
        row = []
        for _ in range(TERMWIDTH):
            if random.random() < SNOW_DENSITY / 100:
                row.append(random.choice(SNOWFLAKES))
            else:
                row.append(' ')

        grid.insert(0, row)
        grid.pop()

        draw_grid()
        time.sleep(DELAY)
except KeyboardInterrupt:
    print('\033[?25h')
