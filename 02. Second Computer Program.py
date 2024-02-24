def main():
    print("This is my second computer program")
    print("By: German Francis Intano") #Program author hard encoded for transparency

    #For user-input
    num1 = int(input("\nEnter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    num3 = int(input("Enter the third integer: "))

    import math

    #For the calculations
    total_sum = num1+num2+num3
    difference = num3-num2
    product = num1*num2*num3
    quotient = num1/num2
    remainder = num2%num1
    square_num = num1**2
    square_root_num = math.sqrt(num3)
    power_num = num2**5

    #Display output
    print("\nThe sum of the three integers is =", total_sum)
    print("The difference between the third and the second integers =", difference)
    print("The product of three integers =", product)
    print("The quotient of the first and second integers =", quotient)
    print("The remainder of the quotient of the second and the first integers =", remainder)
    print("The square of the first integer =", square_num)
    print("The square root of the third integer =", square_root_num)
    print("The second integer raised to the 5th power =", power_num)

    print("\nThank you. Enjoy your day!")

if __name__ == "__main__":
    main()

