print("Hi! This amey!")
print("Use Shift+Enter to get output on terminal")

list = [10,20,20]
list.append(30)
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(len(list))
print("---------------------------")
# ()--> represents tupple
# []-->represents list
print("---------------------------")
for number in 1,2,3,4,5:
     print("The current number is ",number)

print("---------------------------")
for number in range (1, 10, 2):
      print("The current number is \n ", number)

for number in range(1,5):
      print ("The current number is ",number)
print("---------------------------")
for number in range(1,7,2):
      print ("The current number is ",number)
print("---------------------------")
for number in range(5,0,-1):
      print ("The current number is ",number)

      print("---------------------------")



number_of_passengers=5
number_of_baggage=2
security_check=True
for passenger_count in range(1, number_of_passengers+1):
    for baggage_count in range(1,number_of_baggage+1):
        if(security_check==True):
            print("Security check of passenger:", passenger_count, "-- baggage:", baggage_count,"baggage cleared")
        else:
            print("Security check of passenger:", passenger_count, "-- baggage:", baggage_count,"baggage not cleared")

print("----------------------------------------------------------")

for i in range(4):
    for j in range(4):
        print("#",end="")

    print()

    print("---------------------------------------------------------")


 

Number = int(input("Enter the number : "))
Sum = 0

while(Number>0):
     Remainder = Number % 10
     Sum = Sum + Remainder
     Number = Number //10

print("\n Sum of the digit of given number = %d" %Sum)     

print("------------------------------------------------")
for i in range(4):
    for j in range(i+1):
        print("#",end="")

    print()

    
for i in range(4):
    for j in range(4-i):
        print("#",end="")

    print()

    print("-------------------------------------------------------------------------")

num = int(input("Enter the number of rows: "))
for i in range(1,num+1):
    for j in range(1,num-i+1):
        print(end="")
    for j in range(i,0,-1):
        print(j,end="")
    for j in range(2,i+1):
        print(j,end="")
    print()

print('-----------------------------------------------------------------------------')

strl='Hello world'
print(strl)
new  = strl.replace('Hello','Welcome')
print(new)