password = ""
charnum = int(input("How many alphabetic letters would you like to be in your password (max 50)?"))
numbernum = int(input("How many numbers/symbols would you like to be in your password (max 50)?"))
alphalist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
CAPalphalist = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numlist = ['1','2','3','4','5','6','7','8','9','10']
symbollist = ['&','$','!','#','%']
from random import *
somelist = list(range(1,51))
randomlist = [int(uniform(0,25)) for i in somelist]
randomlist2 = [int(uniform(0,9)) for i in somelist]
randomlist3 = [int(uniform(0,5)) for i in somelist]

for i in list(range(1,charnum + 1)):
    x = int(uniform(1,3))
    if x == 1:
        password = password + alphalist[randomlist[i]]
    else:
        password = password + CAPalphalist[randomlist[i]]

for i in list(range(1,numbernum + 1)):
    x = int(uniform(1,3))
    if x == 1:
            password = password + numlist[randomlist2[i]]
    else:
        password = password + symbollist[randomlist3[i]]

print("Your randomly generated password is:" + password)
      
            
    
    
