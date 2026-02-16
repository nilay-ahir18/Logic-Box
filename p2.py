

print("Welcome to the Pattern Generator and Number Analyzer!")
while True:
    print("\nselect option ")
    print("1. Pattern Generator")
    print("2. Number Analyzer")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
    
        rows = int(input("\nEnter the number of rows for the pattern:\n"))

        print("\nPattern:")
        for i in range(1, rows + 1):
             print("*" * i)


    elif choice == "2":

    
        start = int(input("\nEnter the start of the range: "))
        end = int(input("Enter the end of the range: "))

        total = 0

        for num in range(start, end + 1):
            if num % 2 == 0:
                print(f"Number {num} is Even")
            else:
                print(f"Number {num} is Odd")
            total += num

        print(f"Sum of all numbers from {start} to {end} is: {total}")
    elif choice == "3":
        print(" \n Exiting the programe ")
        break
    
    else:
        print("Invalid choice. Please select a valid option.")

    print("\nProgram completed successfully.")
