# x = input(int("Enter a number : "))
# y = input(int("Enter second number : "))
# sum = x - y
# print("The answer is : " , sum)
def matrix(n): 
    m = [[0 for x in range(n)] 
                      for y in range(n)]
    i = n / 2
    j = n - 1
    num = 1
    while num <= (n * n): 
        if i == -1 and j == n:
            j = n - 2
            i = 0
        else:
            if j == n: 
                j = 0 
            if i < 0: 
                i = n - 1
        if m[int(i)][int(j)]:
            j = j - 2
            i = i + 1
            continue
        else: 
            m[int(i)][int(j)] = num 
            num = num + 1
        j = j + 1
        i = i - 1
    print ("Sum of eggs in each row or column and diagonal ",n * (n * n + 1) / 2, "\n") 
    for i in range(0, n): 
        for j in range(0, n): 
            print('%2d ' % (m[i][j]),end = '') 
            if j == n - 1:  
                print()
n=int(input("Number of rows of matrix:"))
matrix(n)
