
#import calendar
#print(calendar.month(2024, 10))



rows=6

for i in range(1, rows):  
        for j in range(1, i + 1):  
            print(i, end=" ")       
        print()


#rows = int(input("Enter the number of rows: "))  

#for num in range(rows+1):  

#        for i in range(num):  
#            print(num, end=" ")       
#        print()


#equilateral pyramid        
rows = int(input("Enter the number of rows: "))  
m = (2*rows)-2

for i in range(0, rows):  
        for j in range(0, m):  
            print(end=" ")
        m -= 1 
        for j in range(0, i+1):  
            print("*",end=" ")              
        print()


#reverse equilateral     
rows = int(input("Enter the number of rows: "))  
m = (2*rows)-2

for i in range(rows-1,-1,-1):  
        for j in range(m,0,-1):  
            print(end=" ")
        m += 1 
        for j in range(0, i+1):  
            print("*",end=" ")              
  
        print()   