


# Create an empty list called my_list.
my_list=[]

#Append the following elements to my_list: 10, 20, 30, 40.

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert the value 15 at the second position in the list.

my_list.insert(1,15)
#list 2 

list_2=[50,60,70]

# Append the following elements to my_list: 10, 20, 30, 40.

my_list.extend(list_2)
print(my_list)

# Remove the last element

my_list.remove(70)
print(my_list)

# sort the list in ascending order

sorted_list=sorted(my_list)
print(sorted_list)


# sorted_list.sort(reverse=True)
# print(sorted_list)

# find and print the index of 30
index=my_list.index(30)
print(index)
