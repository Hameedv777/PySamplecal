#Function Addition
def add(x,y):
    return x+y
#Function to subtract
def subtrct(x,y):
    return x-y
#function to multiplies
def mltyply(x,y):
    return x*y
#Function to Divide
def dvd(x,y):
    return x/y
def moude(x,y):
    return(x%y)

print("Select Operator")
print("1 .Addition")
print("2.Substraction")
print("3.Multiply")
print("4 .Division")

while True:
    choice=input("Enter choice(1/2/3/4/5):")
    if choice in('1','2','3','4','5'):
        try:
            num1=float(input("Enter fist Number:"))
            num2=float(input("Enter second number:"))
        except ValueError:
            print("Invalid input. Please enter a number")
            continue
        if choice=='1':
            print(num1,"+",num2,"=",add(num1,num2))
        elif choice=='2':
            print(num1,"-",num2,"=",subtrct(num1,num2))
        elif choice=='3':
            print(num1,"*",num2,"=",mltyply(num1,num2))
        elif choice=='4':
            print(num1,"/",num2,"=",dvd(num1,num2))
        elif choice=='5':
            print(num1,"%",num2,"=",moude(num1,num2))
 
            nextcalc=input("Do you want another calculation")
            if nextcalc=="no":
                break
else:
    print("Invalid input")









