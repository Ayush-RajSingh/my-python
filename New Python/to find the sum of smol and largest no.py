num = int(input("Enter any number ")) #1465 

small = 10
large = 0

while(num > 0):            #1
    rem = num % 10         #1 % 10 = 1

    if(rem > large):       
        large = rem       #large = 6
    if(rem < small):     
        small = rem      #small = 1
    
    num = num // 10      #1 // 10 = 0

sum = large + small
print("sum is ", sum)
