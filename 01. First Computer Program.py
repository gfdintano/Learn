#Function for main body output
def main():
    print("This is my first computer program")
    print("By: German Francis Intano") #Program author hard encoded to ensure transparency

    #Getting user-information
    first_name = input("\nEnter your first name: ")
    middle_name = input("Enter your middle name: ")
    last_name = input("Enter your last name: ")
    home_address = input("Enter your home address: ")
    city = input("Enter the city which you live in: ")
    favorite_subject = input("Enter your favorite subject: ")

    full_name = f"{first_name} {middle_name} {last_name}"
    full_address = f"{home_address} {city}"

    #Display the information
    print("\nYour Full Name is", full_name)
    print("You live at", full_address)
    print("Your favorite subject is", favorite_subject)

if __name__== "__main__":
    main()