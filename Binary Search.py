from calendar import c
from itertools import count


binary_list = []
size = int(input("Enter size of the binary tree: "))
print("\n")
for i in range (size):
    v = float(input(f"Enter num {i+1}: "))
    binary_list.append(v)

def search(num):
    binary_list.sort()
    L = 0
    U = size
    count = 1
    loop = size
    while loop:
        M = (L + U)//2
        if binary_list[M] == num:
            print(f"Found after {count} times")
            return M
        elif binary_list[M] > num:
            U = M
        elif binary_list[M] < num:
            L = M
        count += 1
        
            
num = float(input("\nEnter a num to search: "))
searched_num_index = search(num)

if searched_num_index:
    print(f"\nNumber found at index: {searched_num_index}")
else:
    print("\nNumber not found!")