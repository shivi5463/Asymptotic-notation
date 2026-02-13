def ONSquare(n):
    iteration=0
    for i in range(0,n):
        for l in range (0,n):
            print("*", end ="")
            iteration+=1
        print("")
    print("/nWhen n is ",n," Iterations = ",iteration,"/n")

ONSquare(5)
ONSquare(4)
ONSquare(3)

print("/nWith every 'n' the time taken equals n^2")
print("0(n^2)")