"Peter Nguyen"
"6/20/2021"
"CIS2348"
"1860823"
"8.10 CIS 2348 LAB: Palindrome"

i = input()
low = 0
high = len(s)-1
result = True
while(low<high):
    if(i[low]==' '):
        low+=1
    elif(i[high]==' '):
        high-=1
    elif(i[low]!=i[high]):
        result = False
        break
    else:
        low+=1
        high-=1
if (result):
    print(i,"is a palindrome")
else:
    print(i, "is not a palindrome")