# num = input("Enter a number: ")
# num = int(num)

# if num % 2 == 0:
#     print("Num is even!")
# else:
#     print("Num is odd!")



pakistani = ["samosa", "daal", "naan"]
chineese = ["egg role", "pot sticker", "fried rice"]
italian = ["pizza", "pasta", "rositto"]

dish = input("Enter a dish name: ")

if dish in pakistani:
    print("This is a Pakistani cousine")
elif dish in chineese:
    print("This is a chineese cousine")
elif dish in italian:
    print("This is italian cousine")
else:
    print("I don't know which dish it is...!")



if "__name__" == "__main__":
    pass