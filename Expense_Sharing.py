def setupExpenses():  # Create a list of people and their expense records
    numPeople = int(input("How many people are there?: "))  # Get the number of people
    people = []
    
    for count in range(numPeople):  # Use 'count' for the range
        name = input(f"Enter name {count + 1}: ").strip()  # Show number while taking input
        people.append(name)
    
    records = {}  # Dictionary to track who owes what

    for payer in people:
        records[payer] = {}  # Create a record for each person
        for receiver in people:
            records[payer][receiver] = 0  # Set initial balance to 0
    
    return people, records


def addExpense(people, records):
    payer = input("Enter the name of the person who paid: ").strip()  # Get the name of the payer

    if payer not in people:  # Check if the name is valid
        print("Invalid name!")
        return
    
    totalAmount = int(round(float(input("Enter the amount paid: "))))  # Get the total amount paid
    splitAmount = round(totalAmount / len(people))  # Split it equally
    
    for person in people:
        if person != payer:
            records[person][payer] += splitAmount  # Others owe this amount
            records[payer][person] -= splitAmount  # Payer's balance is adjusted

    # Adjust records to clear mutual debts
    for debtor in people:
        for creditor in people:
            if debtor != creditor:
                debt = records[debtor][creditor]
                credit = records[creditor][debtor]
                if debt > 0 and credit > 0:
                    minValue = min(debt, credit)
                    records[debtor][creditor] -= minValue  # Reduce what debtor owes
                    records[creditor][debtor] -= minValue  # Reduce what creditor is owed
    
    print("Expense recorded successfully!")

def showRecords(people, records):
    print("\nBalance Sheet:")
    print("\t" + "\t".join(people))

    for debtor in people:
        row = [debtor]  # Start with the person's name
        for creditor in people:
            amount = records[debtor][creditor]
            row.append(f"{amount}" if amount > 0 else "0")  # Show amounts owed
        print("\t".join(row))

def menu(people, records):  # Main menu
    while True:
        print("\nChoose an option:")
        print("1. Add an Expense")
        print("2. Show Expenses")
        print("3. Exit\n")
        choice = int(input("Enter choice: "))  # Get user's choice
        
        if choice == 1:
            addExpense(people, records)
        elif choice == 2:
            showRecords(people, records)
        elif choice == 3:  # Exit the program
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again!")

people, records = setupExpenses()
menu(people, records)
