""" Enter ATM Pin: The program promts the user to enter the correct PIN.
When correct PIN is entered their balance is displayed. The user has three attemps."""
count =  0 #assigning the variable count for attemps allowed
while count < 3: #the loop executes till the attempts are less than 3
    atm_pin = input('Please enter your PIN: ') #user promted to enter PIN
    if atm_pin == '1234':  #if the password is 1234 the balance will get displayed
        print('Your account balance is: XXXX')
        break #the loop closes if the correct PIN is entered
    elif count <= 1 and count <= 3: #if incorrect and the attemp is 1 and/or 2
        count += 1 #an attempt is added to count
        print('Invalid PIN entered. Please try again. You have', {3 - count}, 'attempt(s) left')
        #error message gets printed which shows how many attempts remainin
    else: #at the third attempt the message below gets printed
        print("Attempts exhausted. This account is locked.")
        break
