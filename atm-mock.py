from datetime import datetime
import random

#start program 
#login
#register
#generate account
#operations
#logout
#deposit
#withdrawal
#complaint
#current users should be dictionary

customers = {}

def start():
    print('-----------------------')
    print('Welcome to SAMREH BANK')
    print('-----------------------')
    print('What would you like to do?')
    print("1. Register")
    print("2. Login")

    selectedOption = int(input("Select an option: \n"))

    if (selectedOption == 1):
       register()
    elif (selectedOption == 2):
        login()
    else:
        print("Invalid option selected")
        start()


def register():
    print("Sign up with Samreh Bank")
    print("----------------------------")

    email = input("Enter email address \n")
    first_name = input("First Name: \n")
    last_name = input("Last Name: \n")
    username = input("Create a username: \n")
    password = input("Create a password: \n")

    accountNumber = generatedAccountNumber()

    customers[accountNumber] = [first_name, last_name, email, username, password]

    print("----------------------------")
    print("Account created successfully")
    print(f"Your Account number: {accountNumber}")
    print("----------------------------")
    print("Keep your details safe for hackers")
    print("----------------------------")

    login()


def generatedAccountNumber():
    return random.randrange(0000000000,9999999999)


def login():
    print("----------------------------")
    print("Enter your valid credentials")

    username = input("Username: \n")
    password = input("Password: \n")
    
    for accountNumber, userDetails in customers.items():
        if(accountNumber):
            if(userDetails[3] == username and userDetails[4] == password):
                print("You're logged in successfully")
                bankOperations(userDetails)
            else:
                print("Invalid username or password")
    else:
        print('User not found')


def bankOperations(user):
    print("----------------------------")
    print(f"Welcome {user[0]}")
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(dt_string)
    print("----------------------------")

    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaint')
    print('4. Logout')
    print('5. Exit')

    bankOperationOption = int(input('Please select an option: \n'))

    if(bankOperationOption == 1):
        withdrawOperation()
    elif(bankOperationOption == 2):
        depositOperation()
    elif(bankOperationOption == 3):
        complaintOperation()
    elif(bankOperationOption == 4):
        logout()
    elif(bankOperationOption == 5):
        exit()
    else:
        print('Invalid option selected, please try agian')
        bankOperations(user)


def withdrawOperation():
    withdrawnAmount = int(input('How much would you like to withdraw: \n'))
    print('============================')
    print('Withdrawal successful')
    print(f'Take your cash: {withdrawnAmount} naira')
    anotherTransaction()

def depositOperation():
    accountToDeposit = int(input('Account Number: \n'))
    depositedAmount = int(input('How much would you like to deposit: \n'))
    print('============================')
    print(f'{depositedAmount} naira Deposit to {accountToDeposit} was successful')
    anotherTransaction()


def complaintOperation():
    complainMessage = input('What issue will you like to report? \n')
    print('============================')
    print('Message received')
    print('Thank you for contacting us')
    anotherTransaction()


def logout():
    print("----------------------------")
    print("Logged out")
    login()


def anotherTransaction():
    print("----------------------------")
    print('Do you want to perform another transaction')
    print("----------------------------")

    print('1. Yes')
    print('2. No')

    transactionOption = int(input('Select Transaction: \n'))

    if(transactionOption == 1):
        login()
    elif(transactionOption == 2):
        exit()
    else:
        print('Invalid Transaction selected')
        exit()





start()




    
    

    








