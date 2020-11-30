num = int(input("Enter a number : ")) # take number from user to check


def checkArmstrongNumber(num):
    temp = num
    sum = 0
    n = len(str(num))
    while temp > 0:
        digit = temp % 10
        sum +=digit ** n
        temp //= 10
    if sum == num:
        print(num, " is an Armstrong number.")
    else:
        print(num, " is not an Armstrong number.")
        
checkArmstrongNumber(num) # call the method and pass parameter
