import sys
import os

print('New line and space are escaped(they are not consider as characters).')
user_input = input("Enter the path of your TXT file: ")

assert os.path.exists(user_input), "File does not exist at, "+str(user_input)
f = open(user_input,'r+')

print('\n')

characters = ''
for x in f:
  characters += x

def removeDuplicate(str, n):  
    index = 0
    for i in range(0, n): 
        for j in range(0, i + 1): 
            if (str[i] == str[j]): 
                break
        if (j == i): 
            str[index] = str[i] 
            index += 1
              
    return "".join(str[:index]) 

string= characters
n = len(string)
no_duplicate = removeDuplicate(list(string), n) 

count_1 = 0
for i in characters:
  if i != ' ':       
    count_1 = count_1 + 1

count = 0
list_arr = []

for x in no_duplicate:
  if x != ' ' and x != '\n':      
    count = 0
    for i in characters:
      if i == x: 
        count += 1
    count = (count/count_1) * 100
    list_arr.append([x,count])

chars_pers = '\n\n'
chars_diagram = ''
for value in list_arr:
  chars = ''
  int_value = int(value[1])
  for int_vl in range(int_value):
    chars += '.'  
  chars_diagram += str(value[0]) + '|' + chars + '\n'
  chars_pers += 'The percentage of character "' + value[0] + '" is ' + str(int_value) + '%\n' 

print(chars_diagram)
print(chars_pers)
