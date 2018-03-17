from array import array
print("This program finds the largest number in a list of integers.")
print()
num_list = []
num=0

while (num>=0):
    num = int(input("Please input a integer. (Press -1 to end) ")
    num_list.append(num)
print()
print(num_list)
    largest = num_list[0]
for i in range(len(num_list)):
    if num_list[i]>largest:
            largest = num_list[i]
print("Largest number is {0}".format(largest))
