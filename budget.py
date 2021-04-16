class Budget:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount


    def deposit(self):
        print(f'{self.amount} naira deposited into {self.category} category wallet')


    def withdraw(self):
        print(f'{self.amount} naira withdrawn from {self.category} category wallet')

    
    def balance(self):
        print(f'Your balance is {self.amount} naira in {self.category} category')


    def transfer(self):
        print(f'{self.amount} naira was transfered to {self.category} category')


r1 = Budget('food', 10000)
r2 = Budget('Clothing', 20000)
r3 = Budget('Entertainment', 5000)
r4 = Budget('Food', 8000)


def start():
    print('Welcome to the Budget App')
    print('=========================')

    print('1. Deposit')
    print('2. Withdraw')
    print('3. Check balance')
    print('4. Transfer funds')
    print('5. Exit')

    selectOption = int(input("What would you like to do: \n"))

    if(selectOption == 1):
        r1.deposit()
    elif(selectOption == 2):
        r2.withdraw()
    elif(selectOption == 3):
        r3.balance()
    elif(selectOption == 4):
        r4.transfer()
    elif(selectOption == 5):
        exit()
    else:
        print('Wrong selection')
        exit()



start()


    

    




