"Peter Nguyen"
"6/20/2021"
"CIS2348"
"1860823"
"HW2"

months={ "january":"1","february":"2", "march":"3","april":"4", "may":"5", "june":
    "6","july":"7", "august":"8", "september":"9","october":"10", "november":"11", "december":"12"}

input_file=open('C:\\Users\\Peter\\Desktop\\inputDates.txt', 'r')
output_file=open('C:\\Users\\Peter\\Desktop\\parsedDates.txt','w')

for each in input_file:
    if each != "-1":
        lis = each.split()
        if len(lis) >= 3:
            month = lis[0]
            day = lis[1]
            year = lis[2]

            if month.lower() in months:
                comma = day[-1]
                if comma == ',':
                    day = day[:len(day) - 1]
                    month_number = months[month.lower()]
                    out = month_number+"/"+day+"/"+year

                    output_file.write(out)
                    output_file.write("\n")
output_file.close()
input_file.close()