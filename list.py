# item1 = "bread"
# item2 = "pasta"
# item3 = "fruits"

items = ["bread"," pasta", "fruits", "veggies"]

print(items)


print(items[0])

print(items[1:4])


items[1] = "cookie"    # here element at index 1 will be replaced with the specfified item

print(items)


items.append("butter")   #adding element at the last   because of index

print(items)


items.insert(3, "pasta")

print(items)


food = ["bread", "pasta", "fruits"]

washroom = ["shampoo", "soap"]

mix = food + washroom    #here 2 lists will be concatenated

print(mix)


print(len(mix))


print("bread" in food)

print("pack" in washroom)
