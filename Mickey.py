from random import randint
from pynput.keyboard import Key, Listener
import os

BLANK = "⬜️"
OBSTACLE = "⬛️"
MICKEY = "🐭"
EXIT = "🚪"

grid = [
    [BLANK,BLANK,BLANK,BLANK,BLANK,BLANK],
    [BLANK,BLANK,BLANK,BLANK,BLANK,BLANK],
    [BLANK,BLANK,BLANK,BLANK,BLANK,BLANK],
    [BLANK,BLANK,BLANK,BLANK,BLANK,BLANK],
    [BLANK,BLANK,BLANK,BLANK,BLANK,BLANK],
    [BLANK,BLANK,BLANK,BLANK,BLANK,BLANK]
]

list_of_list = list()
mouse = []

def check_up():
    if mouse[0] != 0:
        row, col = mouse[0], mouse[1]
        if grid[row - 1][col] == BLANK:
            grid[row - 1 ][col] = MICKEY
            grid[row][col] = BLANK
            mouse[0], mouse[1] = row - 1, col
            clear = lambda: os.system("cls")
            clear()
            print_grid(grid)
        elif grid[row - 1][col] == EXIT:
            grid[row - 1 ][col] = MICKEY
            grid[row][col] = BLANK
            mouse[0], mouse[1] = row - 1, col
            clear = lambda: os.system("cls")
            clear()
            print("You Win")
            exit(0)
        else:
            print("You can't move there pal")

def check_down():
    if mouse[0] != 5:
        row, col = mouse[0], mouse[1]
        if grid[row + 1][col] == BLANK:
            grid[row + 1 ][col] = MICKEY
            grid[row][col] = BLANK
            mouse[0], mouse[1] = row + 1, col
            clear = lambda: os.system("cls")
            clear()
            print_grid(grid)
        elif grid[row + 1][col] == EXIT:
            grid[row + 1 ][col] = MICKEY
            grid[row][col] = BLANK
            mouse[0], mouse[1] = row + 1, col
            clear = lambda: os.system("cls")
            clear()
            print("You Win")
            exit(0)
        else:
            print("You can't move there pal")

def check_left():
    if mouse[1] != 0:
        row, col = mouse[0], mouse[1]
        if grid[row][col - 1] == BLANK:
            grid[row][col -1] = MICKEY
            grid[row][col] = BLANK
            mouse[0], mouse[1] = row, col -1
            clear = lambda: os.system("cls")
            clear()
            print_grid(grid)
        elif grid[row][col - 1] == EXIT:
            grid[row][col - 1] = MICKEY
            grid[row][col] = BLANK
            mouse[0], mouse[1] = row, col - 1
            clear = lambda: os.system("cls")
            clear()
            print("You Win")
            exit(0)
        else:
            print("You can't move there pal")

def check_right():
    if mouse[1] != 5:
        row, col = mouse[0], mouse[1]
        if grid[row][col + 1] == BLANK:
            grid[row][col +1] = MICKEY
            grid[row][col] = BLANK
            mouse[0], mouse[1] = row, col +1
            clear = lambda: os.system("cls")
            clear()
            print_grid(grid)
        elif grid[row][col + 1] == EXIT:
            grid[row][col + 1] = MICKEY
            grid[row][col] = BLANK
            mouse[0], mouse[1] = row, col + 1
            clear = lambda: os.system("cls")
            clear()
            print("You Win")
            exit(0)
        else:
            print("You can't move there pal")

def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

def random_location():
    row, col = randint(0,5), randint(0,5)
    #print(row, col)
    return row, col

def add_coordinate(a,b):
    newspace =[a,b]
    list_of_list.append(newspace)

def check_exist(a,b):
    newspace = [a,b]
    for element in list_of_list:
        if element == newspace:
            return True
    return False

def add_element(symbol):
    temp_row, temp_col = random_location()
    if check_exist(temp_row, temp_col) == True:
        add_element(symbol)
    else:
        if symbol == MICKEY:
            mouse.append(temp_row)
            mouse.append(temp_col)
            print(mouse)
        add_coordinate(temp_row, temp_col)
        grid[temp_row][temp_col] = symbol
            

def on_press(key):
    if key == Key.up:
        check_up()
    elif key == Key.down:
        check_down()
    elif key == Key.left:
        check_left()
    elif key == Key.right:
        check_right()
    elif key == Key.esc:
          return False


add_element(MICKEY)
add_element(EXIT)
add_element(OBSTACLE)
add_element(OBSTACLE)
add_element(OBSTACLE)
add_element(OBSTACLE)
add_element(OBSTACLE)
add_element(OBSTACLE)
add_element(OBSTACLE)
clear = lambda: os.system("cls")
clear()
print_grid(grid)

with Listener(on_press=on_press) as listener:
    listener.join()