def repeat_calculation(i):
    return int(i * 2 + 1)
    
    
def space_calculation(x , i):
    return int((x * 2 - 1) / 2 - i)
    
    
    
x = int(input("Enter x: "))
for i in range (x):
    print(" " * space_calculation(x , i) + "*" * repeat_calculation(i))
    
for i in range(x - 2, -1, -1):
    print(" " * space_calculation(x , i) + "*" * repeat_calculation(i))