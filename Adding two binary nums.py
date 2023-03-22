def addBi(num1,num2):
    l = max(len(num1),len(num2))
    num1 = num1.zfill(l)
    num2 = num2.zfill(l)
    total = ""
    carry = 0
    for i in range (l-1,-1,-1):
        c = carry
        c += 1 if num1[i] == "1" else 0
        c += 1 if num2[i] == "1" else 0
        total = ("1" if c%2 == 1 else "0") + total
        carry = 0 if c < 2 else 1

    if carry !=0 : 
        total = "1" + total
    print(f"{num1} + {num2} : {total}")

if __name__ == "__main__":
    num1 = input("Enter 1st num in binary: ")
    num2 = input("Enter 2nd num in binary: ")
    addBi(num1,num2)