def main():
    while True:
        print("This is program to compute simple beam deflection")
        print("By: German Francis Intano")
        print("Created: 24 February 2024")

        print("\nNote the following legend:")
        print("(1) for CONCENTRATED LOAD at CENTER")
        print("(2) for UNIFORMLY DISTRIBUTED THROUGH the beam")
        print("(3) for UNIFORMLY INCREASING LOAD to ONE END")

        print("\nAssumption:")
        print("Leftmost support is origin of 'x'")
        print("Beam is prismatic and homogenous")

        #Getting user-input
        L = float(input("\nEnter LENGTH of simple beam (in m)= "))
        x = float(input("Enter DISTANCE of computed section (in m)= "))
        E = float(input("Enter MODULUS OF ELASTICTY of the section (in MPa) = "))
        I = float(input("Enter MOMENT OF INERTIA of the section (in cm^4) = "))


        while True:
            load_distribution = input("\nType of Load: ").strip()
            if load_distribution in ['1','2','3']:
                load_distribution = int(load_distribution)
                break
            else:
                print("\nPlease see the notes, and use the proper integer.")

        if load_distribution == 1:
            P = float(input("Enter value of CONCENTRATED LOAD (in N) = "))
        elif load_distribution == 2:
            w = float(input("Enter value of UNIFORMLY DISTRIBUTED LOAD (in N/m) = "))
        elif load_distribution == 3:
            u = float(input("Enter value of UNIFORMLY INCRESING LOAD (in N/m) = "))
        else:
            print("\nThat's not a valid option.")
        
        #Calculations
        L_mm = L * 1000
        x_mm = x * 1000
        I_mm4 = I * (10**4)
        

        if load_distribution == 1:
            CONC_mid_x_disp = (P * x_mm / (12 * E * I_mm4)) * (3 * L_mm**2 / 4 - x_mm**2)
            CONC_mid_max_disp_loc = L / 2
            CONC_mid_max_disp = P * L_mm**3 / (48 * E * I_mm4)
            total_disp_x = CONC_mid_x_disp
        elif load_distribution == 2:
            w_Nm = w / 1000
            UDL_x_disp = (w_Nm * x_mm / (24 * E* I_mm4)) * (L_mm**3 - 2 * L_mm*x_mm**2 + x_mm**3)
            UDL_max_disp_loc = L / 2
            UDL_max_disp = 5 * w_Nm * L_mm**4 / (384 * E * I_mm4)
            total_disp_x = UDL_x_disp
        elif load_distribution == 3:
            u_Nm = u / 1000
            UIL_x_disp = (u_Nm * x_mm / (360 * L_mm * E * I_mm4)) * (7 * L_mm**4 - 10 * L_mm**2 * x_mm**2 + 3 * x_mm**4)
            UIL_max_disp_loc = 2 * L / 3
            UIL_max_disp = 0.00652 * u_Nm * L_mm**4 / (E * I_mm4)
            total_disp_x = UIL_x_disp

        print("\nDeflection at {:.3f} M = {:.2f} MM".format(x,total_disp_x))
        if load_distribution == 1:
            print("Max displacement due to CONCENTRATED MISPAN load = {:.2f} MM @ {:.3f} M".format(CONC_mid_max_disp,CONC_mid_max_disp_loc))
        elif load_distribution == 2:
            print("Max displacement due to UNIFORMLY DISTRIBUTED load = {:.2f} MM @ {:.3f} M".format(UDL_max_disp,UDL_max_disp_loc))
        elif load_distribution == 3:
            print("Max displacement due to UNIFOMLY INCREASING load = {:.2f} MM @ {:.3f} M".format(UIL_max_disp,UIL_max_disp_loc))

        while True:
            choice = input("\nWould you like to input another set of values <Y/N>? ").strip().upper()
            if choice == 'Y' or choice == 'N':
                break
            else:
                print("\nInvalid input. Please enter either 'Y' or 'N'")
        if choice == 'N':
            print("\nThank you")

if __name__ == "__main__":
    main()

        
        
