'''
Write a Python program to convert month name toa number of days.
Expected Output:

List of months: January, February, March, April, May, June, July, August
, September, October, November, December
Input the name of Month: February
No. of days: 28/29 days
'''

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']

print ('List of months: January, February, March, April, May, June, July, August, September, '
       'October, November, December ')

user_choice = input("Enter the month: ")

if user_choice == months[0] or user_choice == months[2] or user_choice == months[4] or user_choice == months[6] or \
                user_choice == months[7] or user_choice == months[9] or user_choice == months[11]:
    print ('No. of days: 31 days')
elif user_choice == months[1]:
    print ("No. of days: 28/29 days")
elif user_choice not in months:
    print ("Wrong month name!")
else:
    print ('No. of days: 30 days')