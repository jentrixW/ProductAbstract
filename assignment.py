for i in range (1,31):
    if i % 2 == 0:
        print(i)


number = 1
while(number <31):
    if number % 2 == 0:
        print (number)
    number += 1

budget = 50000
print ("budget: ",budget,"GHC")

marketing =  0.25 * budget
print ("Marketing:", marketing, "GHC")  

operationalExpenses = 0.50 * budget
print ("operationalExpenses:", operationalExpenses, "GHC")

customerAcquisition = 0.25 * budget
print ("customerAcquisition:", customerAcquisition, "GHC")

customers = customerAcquisition / 5
print ("numberOfCustomers:", customers)







