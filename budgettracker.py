#ask for an initial budget at runtime
initial_budget = int(input("Enter the initial budget amount : "))

# List to store expense records
records = []

# Function to handle adding expenses
def expense():
    global initial_budget  # Use the global variable initial_budget
    item = input("Enter your product : ")  # Ask the user for the product name
    amount = int(input("Enter the cost of your product : "))  # Ask the user for the product cost
    # Check if the amount exceeds the current budget
    if amount > initial_budget:
        print("Low Balance! Cannot purchase this product ")
        print("Current balance: ", initial_budget)
    else:
        initial_budget -= amount  # Deduct the amount from the budget
        records.append({item: amount})  # Add the expense to the records list

# Main loop that continuously shows the menu options until the user chooses to exit
while True:
    # Display menu options
    print("Select an option: \n")
    print("1. Enter the expense \n")
    print("2. Show the expense details \n")
    print("3. Exit \n")
    
    # Get the user's choice
    choice = int(input("Enter choice : "))
    
    # Case 1: Enter the expense
    if choice == 1:
        expense()  # Call the expense function to add an expense
        
    # Case 2: Show the expense details
    elif choice == 2:
        if not records:  # Check if there are no records
            print("No records yet")
        else:
            # Display each expense record
            for record in records:
                for item, amount in record.items():
                    print(f"Current expense list: \n{item} : {amount}")
            print("Current balance is:", initial_budget)  # Show the remaining budget
    
    # Case 3: Exit the program
    elif choice == 3:
        print("Exiting Budget Tracker, Good Bye!")  # Print exit message
        break  # Exit the loop and end the program
    
    # Handle invalid choice
    else:
        print("Enter a valid choice")
