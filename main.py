correct_pin = "1234"
balance = 5000
attempts = 0

print("Welcome to vikram ATM")
print("Select Language:")
print("1. English")
print("2. Hindi")
language = input("Enter 1 or 2: ")

if language != "1":
    print("Sorry currently only English language is available.")
    
while attempts < 3:
    pin = input("Enter 4-digit PIN: ")

    if len(pin) != 4:
        print("PIN must be exactly 4 digits")
        continue  
    if pin == correct_pin:
        print("PIN Verified ")
        print("Menu:")
        print("1. Balance Check")
        print("2. Deposit")
        print("3. Withdraw")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            print("Your Balance =", balance)

        elif choice == "2":
            amount = int(input("Enter Amount to Deposit: "))
            balance = balance + amount
            print("Deposit Successful ")
            print("Updated Balance =", balance)

        elif choice == "3":
            amount = int(input("Enter Amount to Withdraw: "))
            if amount > balance:
                print("Not Enough Balance ")
            else:
                balance = balance - amount
                print("Withdraw Successful ")
                print("Updated Balance =", balance)

        else:
            print("Invalid Option ")
        break

    else:
        attempts += 1
        print("Incorrect PIN ")


if attempts == 3:
    print("3 Wrong Attempts ")
    print("Your ATM Card is Locked for 24 Hours ")
