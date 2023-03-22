def Bi_to_De(binary):
    l = len(binary)
    decimal = 0
    for i in range (l):
        decimal += 2**i * (int(binary[l - i - 1]))
    return decimal


binary = input("Enter a binary num: ")

for i in binary:
    if i == '0' or i == '1':
        continue
    else:
        binary = input("\nEnter binary num only: ")
        break

print(f"Binary: {binary}")
print(f"Decimal: {Bi_to_De(binary)}")
