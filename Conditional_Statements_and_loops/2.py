'''
Write a Python program to convert temperatures to and from celsius, fahrenheit.
'''
import re
user_input = input("Enter the data (60C, 25F):").lower()
user_input = re.split('(\d+)',user_input)

temperature = float(str(user_input[0])+str(user_input[1]))
if 'c' in user_input:
    print (str(user_input[0])+str(user_input[1])+'°C is', temperature/5*9+32, 'in Fahrenheit' )
else:
    print(str(user_input[0]) + str(user_input[1]) + '°F is', int(round((temperature - 32) * 5 / 9,0)), 'in Celsius')