r=int(input("Rows: "))

for i in range(1, r + 1):
    
    for j in range(i, 0, -1):
        print(j, end = '')
    
    for j in range(2, i + 1):
        print(j, end = '')
    
    print()