def magic_square(n):
    magicSquare = [[0 for i in range(n)] for j in range(n)]
    MagicNum = n*(n**2 + 1)/2
    print("Magic Number:",MagicNum)

    i = n//2
    j = n-1
    num = n*n
    count = 1
    while(count<=num):
        if(i == -1 and j == n): 
            j = n-2
            i = 0
        else:
            if(j == n):
                j = 0
            if(i<0):
                i = n-1
        if(magicSquare[i][j] != 0):
            j = j-2
            i = i+1
            continue
        else:
            magicSquare[i][j] = count
            count += 1
        
        i = i-1
        j = j+1
    
    return magicSquare


             
        

if __name__ == "__main__":
    n = int(input("Enter a num: "))
    ans = magic_square(n)
    for i in ans:
        print(i)