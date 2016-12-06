'''
Write a Python program to calculate body mass index.
'''

if __name__ == '__main__':

    height = float(raw_input("Enter you height: "))
    weight = float(raw_input("Enter your weight in kg: "))

    if height > 4:
        new_height = float(height/100)
    else:
        new_height = height
    indx = weight / (new_height**2)

    print "="*10
    print "Your body mass index is:", round(indx, 2)

    if  indx <= 18.5:
        print "Underweight"
    elif 18.5 < indx <= 24.9:
        print "Normal weight"
    elif 25 <= indx <= 29.9:
        print "Overweight"
    elif indx >= 30:
        print "Obesity"
    print "="*10
