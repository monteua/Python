'''
Write a Python program to calculate a dog's age in dog's years.
Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
'''

years = float(input("Enter the dog age in human years: "))
dog_years = 0
if years <= 2 and years > 0:
    dog_years = years * 10.5
elif years < 0:
    print ("Age cannot be negative number!")
else:
    dog_years = 10.5 * 2 + (years - 2)  * 4
print ("The dog's age in dog's years is", dog_years)