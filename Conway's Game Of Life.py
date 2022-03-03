from random import choices
import sys, os
from time import sleep
from array import *

node_weights = {"x": 35, " ": 65}
w, h = 50, 50
current_cycle = [[0 for x in range(w)] for y in range(h)]
next_cycle = [[0 for x in range(w)] for y in range(h)]

def percent_return(node):
    val_sum = sum(node.values())
    node_pct = {k: v/val_sum for k, v in node.items()}
    return next(iter(choices(population=list(node_pct), weights=node_pct.values(), k=1)))

def add_random_values(cycle):
    i = 0
    for x in current_cycle:
        j = 0
        for y in x:
            current_cycle[i][j] = percent_return(node_weights)
            j+=1
        i+=1

def print_cycle2(cycle):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
      for row in cycle]))

def is_dead(x, y, next_cycle, current_cycle, w, h):
    if check_neighbours(x,y,current_cycle, w, h) == 3: return "x"
    else: return " "

def check_neighbours(x, y, cycle, w, h):
    life_counter, x_start, y_start, x_end, y_end = 0, 0, 0, 0, 0
    if x == 0: x_start = w
    elif x == w-1: x_end = w
    if y == 0: y_start = h
    elif y == h-1: y_end = h

    if cycle[x-1+x_start][y-1+y_start] == "x": life_counter+=1
    if cycle[x][y-1+y_start] == "x": life_counter+=1
    if cycle[x+1-x_end][y-1+y_start] == "x": life_counter+=1
    if cycle[x-1+x_start][y] == "x": life_counter+=1
    if cycle[x+1-x_end][y] == "x": life_counter+=1
    if cycle[x-1+x_start][y+1-y_end] == "x": life_counter+=1
    if cycle[x][y+1-y_end] == "x": life_counter+=1
    if cycle[x+1-x_end][y+1-y_end] == "x": life_counter+=1
    return life_counter

def is_alive(x, y, next_cycle, current_cycle, w, h):
    if check_neighbours(x,y,current_cycle, w, h) < 2: return " "
    elif check_neighbours(x,y,current_cycle, w, h) > 3: return " "
    else: return "x"

def print_cycle(cycle):
    a = 0
    for k in cycle:
        print(cycle[a])
        a+=1
    print()

print_cycle2(current_cycle)
def get_next(current_cycle, next_cycle, w,h):
    i = 0
    for x in current_cycle:
        j = 0
        for y in x:
            if next_cycle[i][j] == "x":
                next_cycle[i][j] = is_alive(i,j,next_cycle, current_cycle, w, h)
            else: next_cycle[i][j] = is_dead(i,j,next_cycle, current_cycle, w,h)
            j+=1
        i+=1
    return current_cycle, next_cycle

def conways_game_of_life(current_cycle, next_cycle, w, h):
    iterations = 1000
    next_cycle = [row[:] for row in current_cycle]
    while iterations > 0:
        k=3
        while k > 0:
            print()
            k-=1
        print_cycle2(next_cycle)
        get_next(current_cycle, next_cycle, w, h)
        current_cycle = [row[:] for row in next_cycle]
        sleep(.1)
        iterations -= 1

add_random_values(current_cycle)
conways_game_of_life(current_cycle, next_cycle, w, h)
