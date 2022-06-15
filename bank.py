print("Welcome to the bank of the Dillusioners!")
print("Please select an option:")
total = 0
run = True
while run:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    print("5. Loan")
    choice = int(input("Please enter your choice:"))
    if choice == 1:
        amount = int(input("Please enter the amount you want to deposit: "))
        if(amount > 0):
            total += amount
            print(f'Rs.{amount} was deposited to your account and your total balance is Rs.{total}')
        else:
            print("Invalid amount")
    elif choice == 2:
        amount = int(input("Please enter the amount you want to withdraw: "))
        if(amount > 0):
            if amount > total:
                print("Insufficient balance")
            else:
                total -= amount
                print(f'Rs.{amount} was withdrawn from your account and your total balance is Rs.{total}')
        else:
            print("Invalid amount")
    elif choice == 3:
        print(f'Your total balance is Rs.{total}')
    elif choice == 4:
        print("Thank you for using the bank!")
        run = False
    elif choice == 5:
        print("Please enter your loan amount:")
        amount = int(input())
        if amount > 0:
            if amount > total:
                print("Insufficient balance")
            else:
                total -= amount
                print(f'Rs.{amount} was withdrawn from your account and your total balance is Rs.{total}')
        else:
            print("Invalid amount")

