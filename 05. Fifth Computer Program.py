def main():
    while True:
        #Get user-input
        a = int(float(input("\nInput the value of side a of the triangle: ")))
        b = int(float(input("Input the value of side b of the triangle: ")))
        C_degrees = int(float(input("Input the value of angle C of the triangle (in degrees): ")))

        import math

        #Calculation
        C_radians = math.radians(C_degrees)
        C = C_radians
        cos_C = math.cos(C)
        c = round(math.sqrt(a**2 + b**2 - 2*a*b*cos_C),3)
        A = math.asin(a * math.sin(C) / c)
        A_radians = A
        A_degrees = round(math.degrees(A_radians),3)
        B = math.pi - A - C
        B_radians = B
        B_degrees = round(math.degrees(B_radians),3)
        P = round(a + b + c,3)
        s = P/2
        Area = round(math.sqrt(s * (s - a) * (s - b) * (s- c)),3)
    
        #Output
        print("\nThe resulting values are as follows:")
        print("The value of side c = {:.3f}".format(c))
        print("The value of angle A (in degrees) = {:.3f}".format(A_degrees))
        print("The value of angle B (in degrees) = {:.3f}".format(B_degrees))
        print("The perimeter of triangle = {:.3f}".format(P))
        print("The area of the triangle = {:.3f}".format(Area))

        while True:
            choice = input("\nWould you like to input another set of values <Y/N>? ").strip().upper()
            if choice == 'Y' or choice == 'N':
                break
            else:
                print("\nInvalid input. Please enter either 'Y' or 'N'")
        if choice == 'N':
            print("\nThank you")
            break
if __name__ == "__main__":
    main()



    


