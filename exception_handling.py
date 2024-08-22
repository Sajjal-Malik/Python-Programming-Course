x = input("Num1:")
y = input("Num2:")

try:
    z = int(x) / int(y)
# except Exception as e:
except ZeroDivisionError:
    # print("Exception ouccured:", e) 
    print("Division by zero Exception")
    z = None
print("Division is: ", z)