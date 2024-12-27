import time
import getpass
from datetime import date
import function


print("\nWelcome to the Console Banking System\n1. Create Account\n2. Login\n3. Exit\nEnter your choice: ")
user_input = input();
while user_input != '3':
    if user_input == '1':
        account_number = int(time.time() * 1_000_000) % (10**6)
        account_details = str(account_number)
        
        print("\nEnter your name: ")
        account_details += "," + input()
        
        print("\nEnter your initial deposit: ")
        deposit = input()
        
        print(f"\nYour account number: {account_number} (Save this for login)")
        
        password = function.custom_hash(getpass.getpass("Enter a password: "))
        account_details += f",{password},{deposit}"
        
        transaction_details = f"{account_number},Deposit,{deposit},{date.today().isoformat()}"
        
        if function.create_account(account_details):
            print("\nAccount created successfully!")
            if function.add_transaction(transaction_details):
                print(f"\nDeposit successful! Current balance: {deposit}")
            else:
                print("\nDeposit Failed!")
        else:
            print("\nFailed to create account. Please try again!")
                
        
    elif user_input == '2':
        print("\nEnter your account number: ")
        account_number = input()
        password = function.custom_hash(getpass.getpass("Enter your password: "))
        data_dict = function.check_credentials(account_number,password)
        if data_dict:
            print("\nLogin successful!")
            print(f"\n\nWelcome {data_dict[account_number][0]}!\n1. Deposit Money\n2. Withdraw Money\n3. Check Balance\n4. Logout\nEnter your choice: ")
            user_action = input()
            while user_action != '4':
                #Deposit Money
                if user_action == '1':
                    print("\nEnter amount to deposit: ")
                    deposit = input()
                    data_dict[account_number][2] = int(data_dict[account_number][2]) + int(deposit)
                    if function.dict_to_file(data_dict):
                        transaction_details = f"{account_number},Deposit,{deposit},{date.today().isoformat()}"
                        if function.add_transaction(transaction_details):
                            print(f"\nDeposit successful! Current balance: {data_dict[account_number][2]}")
                        else:
                            print("\nDeposit failed, please try again!")
                    else:
                        print("\nDeposit failed, please try again!")
                #Withdraw Money
                elif user_action == '2':
                    print("\nEnter amount to withdraw: ")
                    withdrawal = input()
                    balance = int(data_dict[account_number][2]) - int(withdrawal)
                    if balance >= 0:
                        data_dict[account_number][2] = balance
                        if function.dict_to_file(data_dict):
                            transaction_details = f"{account_number},Withdrawal,{withdrawal},{date.today().isoformat()}"
                            if function.add_transaction(transaction_details):
                                print(f"\nWithdrawal successful! Current balance: {data_dict[account_number][2]}")
                            else:
                                print("\nWithdrawal failed, please try again!")
                        else:
                            print("\nWithdrawal failed, please try again!")
                    else:
                        print("\nInsufficient balance.")
                        
                #Check Balance
                elif user_action == '3':
                    print(f"\nCurrent balance: {data_dict[account_number][2]}")
                else:
                    print("\nInvalid input. Please try again!\n")
                
                print(f"\n\nWelcome {data_dict[account_number][0]}!\n1. Deposit Money\n2. Withdraw Money\n3. Check Balance\n4. Logout\nEnter your choice: ")
                user_action = input()
        else:
            print("\nInvalid account number or password. Please try again!")
        
    else:
        print("\nWrong option")
        
    print("\nWelcome to the Console Banking System\n1. Create Account\n2. Login\n3. Exit\nEnter your choice: ")
    user_input = input();