def Pattern_Print(M):
    for i in range(1, M+1):
        for k in range(M - i):
            print("*", end="")

        for j in range(1, i*2):
            print(i, end="")
        print() 

A = int(input("Enter The Number => "))

Pattern_Print(A)   