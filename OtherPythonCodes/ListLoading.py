#the list
List = ("Mangoes, Carrots, Tomatoes")
#print the list
print(List)

#a list
a = [1,2,3,4,5]
# a  = the list
print(*a)
#say that list printing is seperated by commas
print("printing lists seperated by comas")
#seperate each lis with a comma
print(*a, sep = ",")
#Say print list in new lines
print("printing the lists in new lines")
#do it with /n
print(*a, sep = "/n")

#Print lists of sports
Sports = ("Basketball, Baseball, Soccer,")
#Put x as sports
for x in Sports:
    #Print x
    print(x)


count=0
#print it 1000 times
while (count<1000):
    #prints over 1000 times
    count = count + 1
    #print the lists
    print(List)
    print(a)
