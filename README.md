# Console Banking System

## Overview
The Console Banking System is a simple Python program that simulates basic banking operations such as account creation, login, deposits, withdrawals, and balance checks. It is designed for command-line usage and provides secure password handling and transaction management.

## Features
1. **Create Account**
   - Automatically generates a unique 6-digit account number.
   - Prompts the user to set a password securely.
   - Saves account details along with the initial deposit.

2. **Login**
   - Allows users to log in with their account number and password.
   - Verifies credentials against stored account data.

3. **Deposit Money**
   - Enables users to deposit money into their account.
   - Updates the current balance and records the transaction.

4. **Withdraw Money**
   - Allows users to withdraw money if sufficient balance is available.
   - Updates the balance and records the transaction.

5. **Check Balance**
   - Displays the current balance of the logged-in account.

6. **Secure Password Handling**
   - Passwords are hashed before storage using a custom hash function.

7. **Transaction History**
   - All transactions are recorded with details such as type, amount, and date.

## Prerequisites
- Python 3.x

## Usage
1. Clone or download the repository.
2. Run the program:
   ```bash
   python app.py
   ```

## Example Workflow
### 1. Create an Account
```plaintext
Welcome to the Console Banking System
1. Create Account
2. Login
3. Exit
Enter your choice: 1

Enter your name: John Doe

Enter your initial deposit: 1000

Your account number: 123456 (Save this for login)
Enter a password: ******

Account created successfully!
Deposit successful! Current balance: 1000
```

### 2. Login and Perform Operations
```plaintext
Welcome to the Console Banking System
1. Create Account
2. Login
3. Exit
Enter your choice: 2

Enter your account number: 123456
Enter your password: ******

Login successful!


Welcome John Doe!
1. Deposit Money
2. Withdraw Money
3. Check Balance
4. Logout
Enter your choice: 1

Enter amount to deposit: 500
Deposit successful! Current balance: 1500
```

### 3. Logout
```plaintext
Enter your choice: 4
Logging out...
```

## File Structure
- `app.py`: The main program.
- `function.py`: Contains helper functions for account management and transaction handling.
- `data/accounts.txt`: Stores account information
- `data/transactions.txt` Stores all transactions:

## Security Considerations
- Passwords are hashed before storage to prevent plaintext exposure.
- Transactions are logged to provide a clear record of account activity.

## License
This project is open-source and available under the [MIT License](LICENSE).
