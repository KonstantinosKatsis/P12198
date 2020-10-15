import random
import string
import numpy as np

sos_array = [
        [0] * 10,
        [0] * 10,
        [0] * 10,
        [0] * 10,
        [0] * 10,
        [0] * 10,
        [0] * 10,
        [0] * 10,
        [0] * 10,
        [0] * 10
]
t = ['S', 'O']
for x in range(10):
  for y in range(10):
    sos_array[x][y] = random.choice(t)

print('Array:')
print(np.array(sos_array))
print('\n')

def vertical_function(sos_array):
  string = ''
  count = 0
  for x in range(10):
    string = ''
    for y in range(10):
      string += sos_array[y][x]
      if y == 9:
        index = 0;
        sfr = 0
        for g in range(10):
          strIndex = string.find('SOS',index, index + 3)
          if strIndex > -1:
            sfr += 1
          index += 1
    count += sfr
    print('Vertical line '+ str(x+1) + ":" + str([row[x] for row in sos_array]) + " | number of 'SOS' in column:" + str(sfr) + " | sum:" + str(count))
  print('Vertical counts: ' +str(count))
  
def horizontal_function(sos_array):
  print('\n\n')
  string = ''
  count = 0
  for x in range(10):
    string = '';
    for y in range(10):
      string += sos_array[x][y]
      if y == 9:
        index = 0;
        sfr = 0
        for g in range(10):
          strIndex = string.find('SOS',index, index + 3)
          if strIndex > -1:
            sfr += 1
          index += 1
    count += sfr
    print('Horizontal line '+ str(x+1) + ":" +str(sos_array[x]) + " | 'number of SOS' in row:" + str(sfr) + " | sum:" + str(count))
  print('Horizontal counts: ' + str(count))

def diagonal_function(sos_array):
  print('\n\n')
  string = ''
  count = 0
  diagonal = [sos_array[i][i] for i in range(len(sos_array))]
  print('The diagonal is : ' + str(diagonal))
  
  for value in diagonal:
    string += value
  index = 0;
  for g in range(10):
    strIndex = string.find('SOS',index, index + 3)
    if strIndex > -1:
      count += 1
    index += 1
  print('Diagonal counts: ' +str(count))
        
     
vertical_function(sos_array)
horizontal_function(sos_array)
diagonal_function(sos_array)
        
