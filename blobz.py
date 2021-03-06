
import os
import time
import random
from colorama import Fore, Back, Style
from copy import copy, deepcopy

'''

    Oliver BLOBz. A celular automata in the vein of Conways game of life

    Dedicated to John Conway.

    Copyright (C) 2021 Adam Oliver


    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.


    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the

    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

'''

global num
num = 80
hei = 22
wid = 80


print('#')
print(Fore.RED + '%', end='') #
#print(Fore.LIGHTGREEN + '%') #
print(Fore.YELLOW + '*') #
print(Fore.GREEN + '&') #
print(Fore.BLUE + '$') #
#quit()

global grid
global grid2
grid = [[0 for i in range(wid)] for j in range(hei)] # 80 20 
grid2 = [[0 for i in range(wid)] for j in range(hei)] # 80 20 

# set all grid[x][y] to 6

county = 0
count = 0
for i in grid:
  for j in i:
    grid[county][count] = '6'
    
    count += 1
  count = 0 
  county += 1
# done

# set a few example variables (to be removed)

grid[0][1] = '1'
grid[0][2] = '2'
grid[0][3] = '3'
grid[0][4] = '4'
grid[0][9] = '5'
grid[1][7] = '6'

'''
buckets = ['6'] * num
buckets[9] = '7'
buckets[1] = '8'
buckets[2] = '9'
buckets[3] = '0'
buckets[4] = '1'
'''




# prints the grid2
def print_grid():

  grid2 = grid
  #grid2 = deepcopy(grid)

  count = 0
  for i in grid2:
    for e in i:

      if(e=='1'):print(Fore.BLACK + '#', end='' ) # end='' removes newline
      if(e=='2'):print(Fore.GREEN + '%', end='' ) # 
      if(e=='3'):print(Fore.YELLOW + '*', end='' ) # 
      if(e=='4'):print(Fore.GREEN + '&', end='' ) # 
      if(e=='5'):print(Fore.BLUE + '$', end='' ) # 
      if(e=='6'):print(Fore.BLUE + ' ', end='' ) # 

      if(e=='7'):print(Fore.BLUE + 'i', end='' ) # 

      if(e=='10'):print(Fore.BLACK + 'a', end='' ) # 
      if(e=='11'):print(Fore.BLACK + 'b', end='' ) # 
      if(e=='12'):print(Fore.BLACK + 'c', end='' ) # 
      if(e=='13'):print(Fore.BLACK + 'd', end='' ) # 

      if(e=='14'):print(Fore.GREEN + 'a', end='' ) # 
      if(e=='15'):print(Fore.GREEN + 'b', end='' ) # 
      if(e=='16'):print(Fore.GREEN + 'c', end='' ) # 
      if(e=='17'):print(Fore.GREEN + 'd', end='' ) # 


      if(e=='a'):print(Fore.WHITE + 'a', end='' ) # 
      
      count += 1
      if(count == wid): print(''); count = 0

#
grid[6][9] = '3'
#
print_grid()


###
# this just adds a step
#
def add_cell():

  print('')
  print('')
  
  # change range(1) to change number of new characters
  
  for i in range(3):

    # adds a '#'
    # finds a random place in the grid, adds a cell
    #print(random.randint(1,6))
    x = random.randint(0,hei-1)
    y = random.randint(0,wid-1)

    if( grid[x][y] != 6 ):
      grid[x][y] = '1' #str(random.randint(1,4))
    
    # adds a '%'
    x = random.randint(0,hei-1)
    y = random.randint(0,wid-1)

    if( grid[x][y] != 6 ):
      grid[x][y] = '2' #str(random.randint(1,4))

# this just stops list index out of range error
def numberz_h(thenum):

  #print('[')
  #print('wid thenum')
  #print(wid)
  #print(thenum)

  if(thenum >= wid):
    return wid - 1
  else:
    return thenum
    
def numberz(thenum):

  #print('[')
  #print('hei thenum')
  #print(hei)
  #print(thenum)

  if(thenum >= hei):
    return hei - 1
  else:
    return thenum


  
def a_step():  

  global grid

  ####a
  #y = deepcopy(x)
  grid2 = deepcopy(grid)

  anyhashes = 0

  # grid loop
  count = 0
  for i in grid:
    county = 0
    for j in i:
      #pass

      if( j == '2' ): #
 
        if( random.randint(0,1) == 1 ): # this is cool
          grid2[count][county-1] = str(random.randint(14,17)) #'10' # up
        else:
          grid2[count-1][county] = str(random.randint(14,17)) #'10' # down


      if( j == '14' ): # 
        pass
        if( random.randint(0,1) == 1 ): # this is cool
          grid2[count-1][county] = '15' # left
        else:
          grid2[count][county-1] = '15' # right


      if( j == '15' ): # 
        pass
        if( random.randint(0,1) == 1 ): # this is cool
          grid2[count][ numberz_h(county+1) ] = '16' # down
        else:
          grid2[ numberz(count +1) ][ county ] = '2' # up

      if( j == '16' ): # 
        pass
        if( random.randint(0,1) == 1 ): # this is cool
          grid2[count][ numberz_h(county+1) ] = '17' # down
        else:
          grid2[ numberz(count +1) ][ county ] = '2' # up

      #print(j)
      #print('.', end='')
      if( j == '1' ): #
 
        #print(':D' + str(i))
        anyhashes = 1

        #print('# detected')
        #print(i)
        #pass

        if( random.randint(0,1) == 1 ): # this is cool

          grid2[count][county-1] = str(random.randint(10,13)) #'10' # up

        else:

          grid2[count-1][county] = str(random.randint(10,13)) #'10' # down

      if( j == '10' ): # 
        pass
        if( random.randint(0,1) == 1 ): # this is cool
          grid2[count-1][county] = '11' # left
        else:
          grid2[count][county-1] = '11' # right


      if( j == '11' ): # 
        pass
        if( random.randint(0,1) == 1 ): # this is cool
          grid2[count][ numberz_h(county+1) ] = '12' # down
        else:
          grid2[ numberz(count +1) ][ county ] = '1' # up

      if( j == '12' ): # 
        pass
        if( random.randint(0,1) == 1 ): # this is cool
          grid2[count][ numberz_h(county+1) ] = '13' # down
        else:
          grid2[ numberz(count +1) ][ county ] = '1' # up


      county += 1
      
    count += 1


  if(anyhashes == 0 ):
    print('need a hash')
    add_cell()

  grid = deepcopy(grid2)


add_cell()

while True:
  #
  #
  #print_grid() # to be removed

  #if( random.randint(0,1) == 1 ): # this is cool
    #add_cell()
  
  a_step() # theres a flaw that moves the hash to left

  print_grid()

  #count_blues()

  print('blues on screen: ' + str(1))
  print('greens on screen: ')
  print('')

  time.sleep(.1)#0.1


#print(grid)

quit()










