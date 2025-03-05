def setupExpenses():  # Create a list of participants and their expense records
    numParticipants = int(input("How many participants are there?: "))  # Get the number of participants
    participants = []
    
    for count in range(numParticipants):  # Use 'count' for the range
        participantName = input(f"Enter name {count + 1}: ").strip()  # Show number while taking input
        participants.append(participantName)
    
    expenseRecords = {}  # Dictionary to track who owes what

    for payer in participants:
        expenseRecords[payer] = {}  # Create a record for each participant
        for receiver in participants:
            expenseRecords[payer][receiver] = 0  # Set initial balance to 0
    
    return participants, expenseRecords


def addExpense(participants, expenseRecords):
    payer = input("Enter the name of the participant who paid: ").strip()  # Get the name of the payer

    if payer not in participants:  # Check if the name is valid
        print("Invalid name!")
        return
    
    totalAmount = int(round(float(input("Enter the amount paid: "))))  # Get the total amount paid
    
    print("Who shares the expense?")
    print("1. All participants share the expense")
    print("2. Only some participants share the expense")
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        sharedParticipants = participants.copy()
    elif choice == 2:
        sharedInput = input("Enter names of participants who share the expense (comma separated): ")
        sharedParticipants = [name.strip() for name in sharedInput.split(",") if name.strip() in participants]
        if payer not in sharedParticipants:
            sharedParticipants.append(payer)  # Automatically include the payer
        if len(sharedParticipants) < 2:
            print("At least two participants must share the expense!")
            return
    else:
        print("Invalid choice!")
        return
    
    splitAmount = round(totalAmount / len(sharedParticipants))  # Split among selected participants
    
    for participant in sharedParticipants:
        if participant != payer:
            expenseRecords[participant][payer] += splitAmount  # Others owe this amount
            expenseRecords[payer][participant] -= splitAmount  # Payer's balance is adjusted
    
    # Adjust expenseRecords to clear mutual debts
    for debtor in participants:
        for creditor in participants:
            if debtor != creditor:
                debt = expenseRecords[debtor][creditor]
                credit = expenseRecords[creditor][debtor]
                if debt > 0 and credit > 0:
                    minValue = min(debt, credit)
                    expenseRecords[debtor][creditor] -= minValue  # Reduce what debtor owes
                    expenseRecords[creditor][debtor] -= minValue  # Reduce what creditor is owed
    
    print("Expense recorded successfully!")


def showRecords(participants, expenseRecords):
    print("\nBalance Sheet:")
    print("\t" + "\t".join(participants))

    for debtor in participants:
        row = [debtor]  # Start with the participant's name
        for creditor in participants:
            amount = expenseRecords[debtor][creditor]
            row.append(f"{amount}" if amount > 0 else "0")  # Show amounts owed
        print("\t".join(row))


def menu(participants, expenseRecords):  # Main menu
    while True:
        print("\nChoose an option:")
        print("1. Add an Expense")
        print("2. Show Expenses")
        print("3. Exit\n")
        choice = int(input("Enter choice: "))  # Get user's choice
        
        if choice == 1:
            addExpense(participants, expenseRecords)
        elif choice == 2:
            showRecords(participants, expenseRecords)
        elif choice == 3:  # Exit the program
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again!")


participants, expenseRecords = setupExpenses()
menu(participants, expenseRecords)
