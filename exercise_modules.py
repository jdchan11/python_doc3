from math import pi

def sqrFootage():
    user_length = int(input("What is the length (in feet) of the house? "))
    user_width = int(input("What is the width (in feet) of your house? "))
    user_sqrft = "This house is " + str(user_length * user_width) + " square feet."
    return user_sqrft 


def circOfCircle():
    user_input = input("Are you using the diameter or radius? ")
    if user_input == 'radius':
        rad_input = int(input("What is the radius of the circle? "))
        user_circ = "The circumference of the circle is " + str(2 * pi * rad_input)
    elif user_input == 'diameter':
        diam_input = int(input("What is the diameter of the circle? "))
        user_circ = "The circumference of the circle is " + str(pi * diam_input)
    return user_circ

