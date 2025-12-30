def check_even_odd(number):  # check_even_odd is funtion 
    if number % 2 == 0:   # it divides the user input number by 2 
        return "Number is even"
    else:                          # if the no is even, if not odd
        return "Number is odd"

def main():   # main() is a funtion
    num = int(input("Enter a number: "))  # user input 
    result = check_even_odd(num)  # checking result with check_even_odd(num)
    print(result)

if __name__ == "__main__":   # Starting point of the program
    main()
