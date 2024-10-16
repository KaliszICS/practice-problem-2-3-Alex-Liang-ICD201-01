
'''
Lesson: Else If
Author: Alex Liang
Date Issued: October 16th, 2024
Date Last Modified: October 16th, 2024
'''

def q1(): 
  #Write Assignment code here

  word = str(input('In: '))
  if word[-2:] == 'ey':
    print('-eys')
  elif word[-1:] == 'y':
    print('-ies')
  elif word[-3:] == 'ife':
    print('-ives')
  else:
    print('-s')

def q2(): 
  #Write Assignment code here

  n = int(input('In: '))
  if n > 0:
    print(f'{n} is positive')
  elif n < 0:
    print(f'{n} is negative')

def q3():
  #Write Assignment code here

  side1 = float(input("Input a number: "))
  side2 = float(input("Input a number: "))
  side3 = float(input("Input a number: "))

  if side1 + side2 < side3 or side3 + side2 < side1 or side1 + side3 < side2:
    print('No Triangle')
  elif side1 == side2 and side2 == side3:
    print('Equilateral')
  elif side1 == side2 or side3 == side2 or side3 == side1:
    print('Isosceles')
  else:
    print('Scalene')


#Do not alter the following code
#Comment out the following code when running your tests

#q1()
#q2()
#q3()