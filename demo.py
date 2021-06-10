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

