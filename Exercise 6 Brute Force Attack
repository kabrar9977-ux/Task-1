correct_password = "12345"        # the correct answer of the lock
attempts = 5      # Remainig attempts 5

while attempts > 0: # this while loop repeats the code repeatedly when the condition comes true  
    password = input("Enter the password: ")

    if password == correct_password:
        print("Access granted.")     # if the password is correct
        break
    else:
        attempts = attempts - 1
        if attempts > 0:
            print("Wrong password. Attempts remaining:", attempts) # if the password is wrong with remaining Attempts
        else:
            print("Authorities have been alerted.") # if all attempts are done
