def pascal_function(n):
 
    for line in range(1, n + 2):
        C = 1
        for i in range(1, line + 1):
            print(C, end = " ")
            C = int(C * (line - i) / i)
        print("")
 

n = 4
pascal_function(n)