# 5.8
# Draw Line: A monochrome screen is stored as a single array of bytes, allowing eight consecutive
# pixels to be stored in one byte. The screen has width w, where w is divisible by 8 (that is, no byte will
# be split across rows). The height of the screen, of course, can be derived from the length of the array
# and the width. Implement a function that draws a horizontal line from (x1, y) to (x2, y).
# The method signature should look something like:
# drawLine(byte[] screen, int width, int x1, int x2, int y)
import unittest


def draw_line(screen: list[int], width: object, x1: object, x2: object, y: object) -> object:
    def get_cell(x, y):
        return (x + y * width) // 8 # ex : x=1,y=2. If width=16, we should take element (16+2)/2 = 18/2 = 9
    cell_start = get_cell(x1, y)
    cell_end = get_cell(x2, y)
    if cell_start < cell_end:
        for i in range(cell_start, cell_end+1):
            if i == cell_start:
                pos_in_cell_rev = 7 - x1 % 8
                screen[i] |= 2**(pos_in_cell_rev+1)-1
            elif cell_start < i < cell_end:
                screen[i] = 2**8-1
            else:
                pos_in_cell = x2 % 8
                pos_in_cell_rev = 7 - pos_in_cell
                screen[i] |= 2**(8-pos_in_cell_rev)-1 << pos_in_cell_rev
    elif cell_start == cell_end:
        pos_x1_in_cell_rev = 7 - x1 % 8
        pos_x2_in_cell_rev = 7 - x2 % 8
        number_1 = pos_x1_in_cell_rev - pos_x2_in_cell_rev + 1
        screen[cell_start] |= ((1<<number_1) - 1) << pos_x2_in_cell_rev
    return screen

class TestCase(unittest.TestCase):
    def test(self):
        screen = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        width = 24
        draw_line(screen, width, 21, 21, 0)
        draw_line(screen, width, 2, 21, 1)
        draw_line(screen, width, 10, 12, 2)
        for i in range(len(screen)):
            if i % (width/8) == 0:
                print()
            print(f'{screen[i]:08b}', end='')