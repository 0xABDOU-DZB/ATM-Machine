print('Welcome to ABDOU_DZB Bank ATM')
restart=('Y')
chances = 3 
balance = 999.12
while chances >= 0:
    pin = int(input('Please Enter You 4 Digit Pin: '))
    if pin == (1234)
        print('You entered you pin Correctly')
        print('Please Press 1 For your Balance')
        print('Please Press 2 To Make a Withdrawl')
        print('Please Press 3 To Pay in')
        print('Please Press 4 To Return Card\n')
        while restart not in ('n','NO','no','N'):
            print('Please Press l For Your Balance')
            print('Please Press 2 To Make a Withdrawl')
            print('Please Press 3 To Pay in')
            print('Please Press 4 To Return Card')
            option = int (input('What Would you like to choose?: '))
            if option == 1:
                print('Your Balance is $',balance)
                restart = input('Would You you like to go back? ')
                if restart not in ('n','NO','no','N'):
                    print('Thank You')
                    break
                elif option == 2:
                    option2 = ('y')
                    withdrawl = float(input('How Much Would like to withdraw?
                                        10,20,40,60,80,100 for other enter 1: '))
if withdrawl in [10, 20 ,40, 60, 80, 100]:
                    balance = balance - withdrawl
                    print ('\nYout Balance is now $',balance)
                    restart = input('Would You you like to go back? ')
                    if restart in ('n','NO','no','N',):
                        print('Thank You')
                        break
                elif withdrawl != [10, 20, 40, 60, 80, 100]:
                    print('Invalid Amount, Plwase Re-try\n')
                    restart = ('y')
                elif withdrawl == 1:
                    withdrawl = float(input('Please Enter Desired amount:'))

                elif option == 3:
                    Pay_in = float(input('How Much Would you Like TO pay In? '))
                    balance = balance + Pay_in
                    print ('\nYour Balance is now $' ,balance)
                    restart = input('Would You you like to go back? ')
                    if restart in ('n','NO','no','N',):
                        print('Thank you')
                        break
                    elif option == 4:
                        print('Please wait whilst your card is Returned...\n')
                        print('Thank you for you service')
                        break
                    else:
                        print('Please Enter a correct number. \n')
                        restart = ('y')
          elif pin != ('1234'):
              print('Incorrect Password')
              chances = chances - 1
              if chances == 0:
                  print('\nNo more tries')
                  break