"""
1 2 3
2 4 6
3 6 9
"""
endNum = int(input("Enter how many multiplication tables: "))

for row in range(1, endNum + 1):
    
    for col in range(1, endNum + 1):
        # if it's a single digit
        if(len(str(row*col)) < 2):
            print(f"{row * col} ", end="")
        else:
            print(f"{row * col} ", end="")       
    print() # display a new line