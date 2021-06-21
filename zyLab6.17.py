"Peter Nguyen"
"6/20/2021"
"CIS2348"
"1860823"
"6.17 CIS 2348 LAB: Password modifier"

password=input()
password=list(password)

for i in range(0,len(password)):
    if(password[i]=='i'):
        password[i]='!'
    elif(password[i]=='a'):
        password[i]='@'
    elif(password[i]=='m'):
        password[i]='M'
    elif(password[i]=='B'):
        password[i]='8'
    elif(password[i]=='o'):
        password[i]='.'

strong_password=""
strong_password=strong_password.join(password)
strong_password=strong_password+"q*s"

print(strong_password)