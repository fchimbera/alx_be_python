pattern_size =int(input("Enter the size of the pattern: "))
#added nested for loops to create pattern
for x in range(1, pattern_size + 1):
    for y in range(1, pattern_size + 1):
        print("*",end="")
    print("")