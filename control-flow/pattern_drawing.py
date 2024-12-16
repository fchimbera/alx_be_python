pattern_size =int(input("Enter the size of the pattern: "))
#added nested for loops to create pattern
x = 1
while x <= pattern_size:
    y = 1
    while y <= pattern_size:
        print("*",end="")
        y += 1
    print("")
    x += 1